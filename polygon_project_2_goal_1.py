import math

class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError("Polygon must have at least three sides.")
        self._n = n
        self._R = R
        self._interior_angle = None
        self._side_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None
        
    def __repr__(self):
        return f"Polygon(n={self._n}, R={self._R})"
    
    @property
    def count_vertices(self):
        return self._n
        
    @property
    def count_edges(self):
        return self._n
    
    @property
    def circumradius(self):
        return self._R
    
    @property
    def interior_angle(self):
    if self._interior_angle is None:
        self._interior_angle = (self._n - 2) * 180/_n
    return self._interior_angle
        
    @property
    def side_length(self):
        if self._side_length is None:
            self._side_length = 2 * self._R * math.sin(math.pi / self._n)
        return self._side_length
        
    @property
    def apothem(self):
        if self._apothem is None:
            self._apothem = self._R * math.cos(math.pi / self._n)
        return self._apothem
    
    @property
    def area(self):
        if self._area is None:
            self._area = self._n / 2 * self.side_length * self.apothem
        return self._area
        
    @property
    def perimeter(self):
        if self._perimeter is None:
            self._n * self.side_length
        return self._perimeter
        
    # allows us to use == between Polygons
    @property
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
    
    # allows us to use operators >, <
    def __gt__(self, other):
        if isinstance(other, Polygon):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented