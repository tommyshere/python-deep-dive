class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
pt = Point2D(10, 20)
distance = sqrt(pt.x ** 2 + pt.y ** 2)
# Much more readable

# when using a class __repr__, __eq__ is the least that should implemented

# but screw class objects for tuples, we'll use namedtuples
# it is a function, that generate a nw class
Pt2D = namedtuple("Point2D", ["x", "y"])
Pt2D = namedTuple("Point2D", "x, y") # same as first line
Pt2D = namedTuple("Point2D", "x y")
# it's creating a class Point2D with attributes x and y
# ** cannot use _ as the beginning of a variable name
# to create a tuple call the variable name not the class String name
pt = Pt2D(10, 20)
# because attributes were named in the beginning
pt._asdict()
# will give a dictionary 

# Tuples are immutable so a new object needs to be made
# BUT there's a a built-in _replace method
djia = djia._replace(day=26, high=26_459, close=26_394)

# Extending a tuple
Stock = namedtuple("Stock", "symbol year month day open high low close")
StockExt = namedTuple("StockExt", Stock._fields + ("previous_close", ))
# OR
djia_ext = StockExt._make(djia + (26_000, )) # has to be iterable

# DocStrings
# Overriding
Point2D.__doc__ = "String"
Point2D.x.__doc__ = "attribute string"

# Default Values, using Prototype
Vector2D = namedtuple("Vector2D", "x1 y1 x2 y2 origin_x origin_y")
vector_zero = Vector2D(x1=0, y1=0, y2=0, origin_x=0, origin_y=0)
# or vector_zero = Vector2D(0, 0, 0, 0, 0, 0)
v1 = vector_zero._replace(x1=10, y1=10, y2=20, origin_x=0, origin_y=0)

# using __defaults__
# defaults are right aligned!
Vector2D = namedtuple("Vector2D", "x1 y1 x2 y2 origin_x origin_y")
Vector2D.__new__.__defaults__ = (0, 1) # (x1, y1, x2, y2, origin_x=0, origin_y=1)
v1 = Vector2D(10, 10, 20, 20)
# x1=10, y1=10, x2=20, y2=20, origin_x=0, origin_y=1
