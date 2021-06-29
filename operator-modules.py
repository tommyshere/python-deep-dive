# itemgetter
# have to set with which index you want first
f = itemgetter(1)
# will always get index = 1
s = [1, 2, 3]
f(s) # 2
s = 'python'
f(s) # y

# attrgetter
# same as itemgetter but for objects
f = attrgetter('a')
# takes moultiple params
f = attrgetter('a', 'c')
# all in one
attrgetter('a', 'b')(my_obj)
