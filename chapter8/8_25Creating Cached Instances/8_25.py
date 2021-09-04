'''
weakref
weakref.WeakValueDictionary
'''

import logging
a = logging.getLogger('foo')
b = logging.getLogger('bar')
print( a is b )
c = logging.getLogger('foo')
print( a is c ) #True.same name logger is same instance

# The class in question
class Spam:
    def __init__(self, name):
        self.name = name
# Caching support
import weakref
_spam_cache = weakref.WeakValueDictionary()
def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s

a = get_spam('foo')
b = get_spam('bar')
print( a is b )
c = get_spam('foo')
print( a is c )

# use new
class Spam:
    _spam_cache = weakref.WeakValueDictionary()
    def __new__(cls, name):
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super().__new__(cls)
            cls._spam_cache[name] = self
        return self
    def __init__(self, name):
        print('Initializing Spam')
        self.name = name

s = Spam('Dave')
t = Spam('Dave')
print( s is t )