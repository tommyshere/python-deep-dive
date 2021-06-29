# Python currying
# start off with this
def add(a, b):
    return a + b


def make_adder(a):
    return lambda b: add(a, b)


add_5 = make_adder(5)  # sets 5 as a
add_5(10)  # sets 10 as b
# 15

# BUT there's functools.partial
from functools import partial
# first parameter is the function
# second parameter is the initial value, so it will be a
add_6 = partial(add, 6)
add_6(10)  # sets 10 as b
# 16
