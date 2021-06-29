# when writing functions with *args keywords are needed
def func1(*args, d):
	print(args, d)
	
# d HAS to be keyword argument
func1(1, 2, 3, d='a')

# positional vs keyword arguments!

# when you do something like
def func2(a, b, *, d):
    print(a, b, d)
# you are forcing users to ensure d is a keyword argument
func2(2, 3, d=4)

def func3(*, d, **kwargs):
    pass
   
func(d=1, a=2, b=3)
# d = 1, kwargs = {'a': 2, 'b': 3}

func(d=1)
# d = 1