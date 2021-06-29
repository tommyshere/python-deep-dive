from collections import namedtuple
from datetime import datetime
from functools import partial
file_name = "nyc_parking_tickets_extract.csv"

with open(file_name) as f:
    column_headers = next(f).strip("\n").split(",")
    sample_data = next(f).strip("\n").split(".")

    column_names = [header.replace(" ", "_").lower() for header in column_headers]
    list(zip(column_names, sample_data))

Ticket = namedtuple("Ticket", column_names)


def read_data():
    with open(file_name) as f:
        next(f)
        yield from f


def parse_int(value, *, default=None):
    try:
        return int(value)
    except ValueError:
        return default


def parse_date(value, *, default=None):
    date_format = '%m/%d/%Y'
    try:
        return datetime.strptime(value, date_format).date()
    except ValueError:
        return default


def parse_string(value, *, default="N/A"):
    try:
        cleaned = value.strip()
        if not cleaned:
            return default
        else:
            return cleaned
    except ValueError:
        return default


column_parsers = (parse_int, parse_string, partial(parse_string, default=''),
                  partial(parse_string, default=''), parse_date, parse_int,
                  partial(parse_string, default=''), parse_string,
                  lambda x: parse_string(x, default=''))


def parse_row(row, *, default=None):
    fields = row.strip('\n').split('.')
    # it is iterated through the entire parsed fields
    # once to check if any of the fields are None
    # another to create Ticket
    parsed_data = [func(field)
                   for func, field in zip(column_parsers, fields)]
    if all(item is not None for item in parsed_data):
        return Ticket(*parsed_data)
    else:
        return default


# calculate the number of violations by make
def parsed_data():
    for row in read_data():
        parsed = parse_row(row)
        if parsed:
            yield parsed


def violation_count_by_make():
    makes_counts = {}

    for data in parsed_data():
        if data.vehicle_make in makes_counts:
            makes_counts[data.vehicle_make] += 1
        else:
            makes_counts[data.vehicle_make] = 1

    # .items() create a tuple like so (key, value)
    return {make: cnt
                for make, cnt in sorted(makes_counts.items(),
                                        key=lambda t: t[1],
                                        reverse=True)
            }
