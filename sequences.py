s[i]
s[i:j] # including i, but not j
s[i:j:k] # including i, but not j, in steps of k

# NOT a mutation, as it creates a new object
names = ["Eric", "John"]
names = names + ["Michael"]

# IS mutation
names = ["Eric", "John"]
names.append("Michael")

s[i] = x # replace
s[i:j] = s2 # slice replaced by s2
del s[i] # removes at index
del s[i:j] # removes entire slice

j = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s2 = ['a', 'b', 'c']
j[0:9:4] # [0, 4, 8]
# it replaces those values, but it HAS to be the same length
# or ValueError
j[0:9:4] = s2 # ['a', 1, 2, 3, 'b', 5, 6, 7, 'c', 9, 10]

# Deleting a slice
j[0:3] = []
j = [3, 4, 5, 6, 7, 8, 9, 10]

# Insertion
l = [1, 2, 3]
l[1:1] = "abc" # [1, 'a', 'b', 'c', 2, 3]
# but if given a range it will replace 
l[0:1] # ['a', 'b', 'c', 2, 3]


s.clear()
s.insert(i, x)
s.extend(iterable) # requires an iterable, different than append
s.pop(i) # removes and returns element at index i
s.remove(x) # remove a specific object (x)
s.reverse() # in-place reversal
s.copy() # shallow copy
