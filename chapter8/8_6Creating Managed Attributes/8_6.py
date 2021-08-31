'''
You want to add extra processing (e.g., type checking or validation) to the getting or
setting of an instance attribute
使用@property声明属性 @name setter做set类型检查等
不用写大量的重复代码，比如setter都有共同的类型检查代码
'''
class Person:
    def __init__(self, first_name):
        self.first_name = first_name
    # Getter function
    @property
    def first_name(self):
        return self._first_name
    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

a = Person('Guido')
print(a.first_name ) #function as property
try:
    a.first_name = 42
except Exception as e:
    print( e )

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def area(self):
        return math.pi * self.radius ** 2
    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(4.0)
print( c.radius )
print( c.area )