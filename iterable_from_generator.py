# Generators become exhausted
# they return a new generator when called
def squares(n):
    for i in range(n):
        yield i ** 2


sq = squares(5)  # sq is a new generator (or iterator)
l = list(sq)  # this becomes exhausted
l = list(sq)  # 2nd time will return []

sq = squares(5)
enum1 = enumerate(sq)  # enumerate is lazy
next(sq)  # 0
next(sq)  # 1
list(enum1)  # starts at [(0, 4), (0, 9), (0, 16)]
# enum starts at when it's invoked because enumerator is lazy

# so an iterable is required
class Squares:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return squares(self.n)


sq = Squares(5)
l1 = list(sq)  # [0, 1, 4, 9, 16]
l2 = list(sq)  # [0, 1, 4, 9, 16]
# have the __iter__ like this ensures a new iterator is made
