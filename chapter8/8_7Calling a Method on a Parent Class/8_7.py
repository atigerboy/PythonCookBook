class A:
    def spam(self):
        print('A.spam')
class B(A):
    def spam(self):
        print('B.spam')
        super().spam()
class C:
    def spam(self):
        print('C.spam')

class D(A, C):
    pass

b = B()
#print( b.__mro__ )
print( b.spam() )
d = D()
#print( d.__mro__ ) #no mro attribute
print( d.spam() )

#override any of Python's special methods
class Proxy:
    def __init__(self,obj):
        self._obj = obj

    #Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)
    #Delegate attribute assignment
    def __setattr__(self, key, value):
        if key.startwith('_'):
            super().__setattr__(key, value) #call original __setattr__
        else:
            setattr(self._obj, key, value)