# shit ton of code to write for iterators and iterable
# emit, pause, resume?
yield
# it emits a value, but the fn is in a suspended state
# next will resume from the yield
# the moment a fn uses yield, it is a generator fn
# and returns a generator object
def my_func():
    yield 1
    yield 2
    yield 3

next(gen) # 1
next(gen) # 2
next(gen) # 3
next(gen) # StopIteration

# generators = iterators
# way easier than writing __iter__ and __next__ in a class
def factorials(n):
    for i in range(n):
        yield math.factorial(i)

