'''
You have a collection of generally useful methods that you would like to make available
for extending the functionality of other class definitions. However, the classes where
the methods might be added aren’t necessarily related to one another via inheritance.
Thus, you can’t just attach the methods to a common base class.
不修改基类来扩展class的方式
两种实现的方式不同，作为辅助的类近似property的写法
'''
class LoggedMappingMixin:
    '''Add logging to get/set/delete operations for debugging'''
    __slots__ = ()#what?
    def __getitem__(self, item):
        print('Getting '+str(item))
        return super().__getitem__(item)
    
    def __setitem__(self, key, value):
        print('Setting {}={!r}'.format( key, value))
        return super().__setitem__(key, value)
    def __delitem__(self, key):
        print('Deleting ' + str( key ) )
        return  super(LoggedMappingMixin, self).__delitem__(key)

class SetOnceMappingMixin:
    '''Only allow a key to be set once'''
    __slots__ = ()
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super(SetOnceMappingMixin, self).__setitem__(key, value)

class StringKeysMappingMixin:
    '''Restrict keys to string only'''
    __slots__ = ()
    def __setitem__(self, key, value):
        if not isinstance( key , str ):
            raise  KeyError('Keys must be strings')
        return super(StringKeysMappingMixin, self).__setitem__(key, value )

#first mixin, second defualt class
class LoggedDict( LoggedMappingMixin, dict):
    pass
d = LoggedDict()
d['x'] = 23 #效果近似warps function
print( d['x'] )
del d['x']

from collections import defaultdict
#defaultdict use container(list,set) for extend key values
class SetOnceDefaultDict( SetOnceMappingMixin, defaultdict ):
    pass
d = SetOnceDefaultDict(list)
d['x'].append(2)
d['x'].append(3)
d['x'].append(4)
d['x'].append(5)
try:
    d['x'] = 24
except KeyError as err:
    print( err )

from collections import OrderedDict
class StringOrderedDict( StringKeysMappingMixin, SetOnceMappingMixin, OrderedDict):
    pass

d = StringOrderedDict()
d['x'] = 23
try:
    d[42] = 10
except Exception as err:
    print( err )

try:
    d['x'] = 42
except KeyError as err:
    print( err )

#Method 2,Property

def LoggedMapping(cls):
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__
    def __getitem__(self, key):
        print('Getting ' + str(key))
        return cls_getitem(self, key)
    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return cls_setitem(self, key, value)
    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return cls_delitem(self, key)
    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__
    return cls #very import!!!

@LoggedMapping
class LoggedDict(dict):
    pass

d = LoggedDict()
d['x'] = 23
print( d['x'] )
del d['x']