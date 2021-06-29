# iterable is created once
# iterator is created every time for a fresh iteration

class Cities:
    def __init__(self):
        self._cities = ['Paris', 'Berlin', 'Rome', 'London']
        self._index = 0
        
    def __len__(self):
        return len(self._cities)
        
class CityIterator:
    def __init__(self, cities):
        self._cities = cities
        self._index = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self._index >= len(self._cities):
            raise StopIteration
        else:
            item = self._cities[self._index]
            self._index += 1
            return item
            
# working together:
cities = Cities()
city_iterator = CityIterator(cities)
for city in cities_iterator:
    print(city)

# after this city_iterator is exhausted
# if it needs to reiterate the collection, create a new instance of CityIterator
# but we don't want to create a new iterator EVERY SINGLE TIME
# THUS the ITERABLE
def __iter__(self):
    return CityIterator(self)

# ITERABLE is an object that implements __iter__ and returns an iterator
# ITERATOR implements __iter__ and __next__

# Python uses the iter() built-in function
# that (kind of) calls the __iter__ method (if no __iter__ then it looks for __getitem__)
# iter(collection)

# iter(callable, sentinel)
# iter will call next until it reaches the sentinel value

# __iter__ can also work in use of for loops

# reverse
# both __getitem__ and __len__ must be implemeneted
# or override __reversed__
for item in reversed(seq)
    print(item)
    
# but custom iterables, it needs reversed() will not work
# it will look for reversed() (implement a reverse iterator ourselves)
# if no __reversed__ it will look for __getitem__ and __len__