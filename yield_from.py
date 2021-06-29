# often need to delegage yielding elements to another iterator
def read_all_data():
    for file in ('file1.csv', 'file2.csv'):
        with open(file) as f:
            for line in f:
                yield line


# INSTEAD:
def read_all_data():
    for file in ('file1.csv', 'file2.csv'):
        with open(file) as f:
            yield from f
