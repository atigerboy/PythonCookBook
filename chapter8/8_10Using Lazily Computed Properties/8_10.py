class lazyproperty:
    def __init__(self, func):
        self.func = func
    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__,value)
            return value

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print("Computing area")
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2*math.pi*self.radius

c = Circle(4.0)

print( c.radius )
print( c.area )
print( c.perimeter )
print( c.area )
print( c.perimeter )

c.radius = 5.0
#wrong~~
print( c.radius )
print( c.area )
print( c.perimeter )

#right
del c.area
del c.perimeter
print( c.radius )
print( c.area )
print( c.perimeter )
print( c.area )
print( c.perimeter )

#area, perimeter 能被修改~
c.area = 5 #ok but wrong~

def lazyproperty(func): #why it works?
    name = '_lazy_' + func.__name__
    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value
    return lazy
class Circle2:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print("Computing area")
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2*math.pi*self.radius


c = Circle2(4.0)
print( vars( c ) )
print( c.area )
print( vars( c ) )

