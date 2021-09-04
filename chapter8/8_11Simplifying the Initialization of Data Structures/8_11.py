'''
simplify __init__ function
'''
import  math
class Structure:
    #Class variable that specified expected fields
    _fields =[]
    def __init__(self,*args ,**kwargs): #args for parameter, kwargs for key=value parameter
        if len( args ) > len(self._fields ):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        #set the arguments
        for name, value in zip( self._fields, args):
            setattr(self, name, value)

        #set the remaining keyword arguments
        if name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))

        # Set the additional arguments (if any)
        for name, value in kwargs.items():
            setattr( self, name, value)



# Example class definitions
if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']
    class Point(Structure):
        _fields = ['x','y']
    class Circle(Structure):
        _fields = ['radius']
        def area(self):
            return math.pi * self.radius ** 2
    s = Stock('ACME', shares=50, price=91.1,date='8/2/2012')
    print( vars( s ) )

