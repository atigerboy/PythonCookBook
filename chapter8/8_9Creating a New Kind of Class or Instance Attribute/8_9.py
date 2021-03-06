#Descriptor attribute for an integer type-checked attribute
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self,instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

#how to use
'''To use a descriptor, instances of the descriptor are placed into a class definition as class
variable'''
class Point:
    x = Integer('x')
    y = Integer('y')
    def __init__(self,x, y):
        self.x = x
        self.y = y

p = Point(2,3)
print( vars(p) )
print( p.x, p.y, p.x + p.y )
print('Point.x is {0!r}'.format( Point.x ))

#more common usage
# Descriptor for a type-checked attribute
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value
    def __delete__(self, instance):
        del instance.__dict__[self.name]
# Class decorator that applies it to selected attributes
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            # Attach a Typed descriptor to the class
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate

# Example use
@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s = Stock('ABC',2,3.4)
s.shares = 1000
try:
    s.price = 'over'
except :
    pass
print( s.price )

#type hint is not strict restricted!!
class Stock2:
    def __init__(self, name:str, shares:int, price:int):
        self.name:str = name
        self.shares:int = shares
        self.price:int = price

s = Stock2('ABC',2,3.4)
s.shares = 1000
try:
    s.price = 'over'
except :
    pass
print( s.price )