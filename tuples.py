# unpacking a tuple
new_york = ('New York', 'USA', 8_500_000)
city, country, population = new_york

# just want city and population
city, _, population = new_york
# underscore is just a dummy variable
# but conventionally underscore is used to ignore 

record = (1, 2, 3, 4, 5)
one, two *_, five = record
# *_ is *args and packs 3, 4 into a list and allows to skip to 5