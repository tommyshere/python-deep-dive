# Using *
l1 = [1, 2, 3]
l2 = [1, 2, 3]
l = [*l1, *l2]
# l = [1, 2, 3, 1, 2, 3]

# Using **
# Can only be used on right hand side
d1 = {'p': 1, 'y': 2}
d2 = ('t': 3, 'h': 4}
d = {**d1, **d2}
# d = {'p': 1, 'y': 2, 't': 3, 'h': 4}
# if there are same keys then it overwrites depending when the ** comes up
d1 = {'a': 1, 'b': 2}
{'a': 10, 'c': 3, **d1} #overwrites the 'a' to 1
{**d1, 'a':10, 'c':3} # does not overwrite

def func(a, b, c):
    pass
  
l = [10, 20, 30]

func(*l)
# thus *args
# should be useful