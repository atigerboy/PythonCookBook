''' Base Class method Proxy'''

#method 1, not recommand!
class A:
    def spam(self, x):
        pass
    def foo(self):
        pass
class B:
    def __init__(self):
        self._a = A()
    def spam(self, x):
        # Delegate to the internal self._a instance
        return self._a.spam(x)
    def foo(self):
        # Delegate to the internal self._a instance
        return self._a.foo()
    def bar(self):
        pass

#method 2, better
class A:
    def spam(self, x):
        pass
    def foo(self):
        pass
class B:
    def __init__(self):
        self._a = A()

    def bar(self):
        pass
    #Expose all of the methods defined on Class A,like virtual method fields filled
    def __getattr__(self, item):
        return getattr( self._a, item )

#method 3, common Proxy
# A proxy class that wraps around another object, but
# exposes its public attributes
class Proxy:
    def __init__(self, obj):
        self._obj = obj
    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        print('getattr:', name)
        return getattr(self._obj, name)
    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print('setattr:', name, value)
            setattr(self._obj, name, value)
    # Delegate attribute deletion
    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('delattr:', name)
            delattr(self._obj, name)

class Spam:
    def __init__(self, x):
        self.x = x
    def bar(self, y):
        print('Spam.bar:', self.x, y)

# Create an instance
s = Spam(2)
# Create a proxy around it
p = Proxy(s)
# Access the proxy
print(p.x) # Outputs 2
p.bar(3) # Outputs "Spam.bar: 2 3"
p.x = 37 # Changes s.x to 37

#Example for ListLike
'''TODO:: All functions starts with __ must defined by hand~~'''
class ListLike:
    def __init__(self):
        self._items = []
    def __getattr__(self, name):
        return getattr(self._items, name)
    # Added special methods to support certain list operations
    def __len__(self):
        return len(self._items)
    def __getitem__(self, index):
        return self._items[index]
    def __setitem__(self, index, value):
        self._items[index] = value
    def __delitem__(self, index):
        del self._items[index]