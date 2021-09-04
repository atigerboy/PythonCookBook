#Base Class, Uses a descriptor to set a value
class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr( self, key, value)
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

#Descriptor for enforcing types
class Typed( Descriptor ):
    expected_type = type( None )

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise  TypeError('expected '+str(self.expected_type ) )
        super().__set__(instance, value)

#Descriptor for enforcing values
class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise  ValueError('Expected >=0 ')
        super().__set__( instance, value )
#Descriptor for enforcing size
class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise  TypeError('missing size option')
        super().__init__(name, **opts )
    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError( 'size must be < ' + str( self.size ) )
        super().__set__(instance, value)

class Integer(Typed):
    expected_type = int

class UnsignedInteger( Integer, Unsigned):
    pass

class Float(Typed):
    expected_type = float

class UnsignedFloat( Float, Unsigned):
    pass

class String(Typed):
    expected_type = str

class SizedString( String, MaxSized):
    pass

#Method 1
class Stock:
    #Specify constraints
    name = SizedString('name', size=8)
    shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

print('Method 1')
s = Stock('ACME', 50, 91.1)
print( s.name )
s.shares = 75
print( s.shares)
try:
    s.shares = -1
except:
    pass
print( s.shares )

try:
    s.name = 'AAAABBBC'
except:
    pass
print( s.name )
'''
There are some techniques that can be used to simplify the specification of constraints
in classes. One approach is to use a class decorator
'''
#Class decorator to apply constraints
def check_attributes(**kwargs ):
    def decorate( cls ):
        for key,value in kwargs.items():
            if isinstance( value, Descriptor ):
                value.name = key
                setattr(cls, key , value)
            else:
                setattr(cls, key, value(key) )
        return cls
    return decorate

#Example
@check_attributes(
    name=SizedString(size=8),
    shares=UnsignedInteger,
    price=UnsignedFloat
)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

print('Method 2')
s = Stock('ACME', 50, 91.1)
print( s.name )
s.shares = 75
print( s.shares)
try:
    s.shares = -1
except:
    pass
print( s.shares )

try:
    s.name = 'AAAABBBC'
except:
    pass
print( s.name )

#A metaclass that applies checking Method3
class checkedmeta( type ):
    def __new__(cls, clsname, bases, methods ):
        #Attach attribute names to the descriptors
        for key, value in methods.items():
            if isinstance( value, Descriptor ):
                value.name = key
        return type.__new__(cls, clsname, bases, methods)
# Example
class Stock(metaclass=checkedmeta):
    #default name eq name,better than method1
    name = SizedString(size=8)
    shares = UnsignedInteger()
    price = UnsignedFloat()
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

print('Method 3')
s = Stock('ACME', 50, 91.1)
print( s.name )
s.shares = 75
print( s.shares)
try:
    s.shares = -1
except:
    pass
print( s.shares )

try:
    s.name = 'AAAABBBC'
except:
    pass
print( s.name )

#Normal
class Point:
    x = Integer('x')
    y = Integer('y')

#MetaClass
class Point(metaclass=checkedmeta):
    x = Integer()
    y = Integer()

#use property functions~ TODO:: Change Typed,Unsigned,MaxSized as Method,
