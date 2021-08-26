import json

data = {
'name' : 'ACME',
'shares' : 100,
'price' : 542.23
}
json_str = json.dumps(data)# dumps for multiline

print( json_str )

# Writing JSON data
with open('data.json', 'w') as f:
    json.dump( data, f )

# Reading data back
with open('data.json', 'r') as f:
    data = json.load( f )
    print( data )

from urllib.request import urlopen
import  json

try:

    u = urlopen('https://en.wikipedia.org/wiki/IEEE_754-1985#NaN')
    resp = json.loads(u.read().decode('utf-8'))
    from pprint import  pprint #pprint for complex print

    pprint( resp )
except:
    pass

s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)
print( data, data['name'], data['shares'], data['price'])

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

data = json.loads( s, object_hook=JSONObject)
print( data, data.name, data.shares, data.price )

data = {
'name' : 'ACME',
'shares' : 100,
'price' : 542.23
}
#if json loads using object hook, dumps throw error~
print( json.dumps( data ))
print( json.dumps( data, indent=4))
print( json.dumps( data, sort_keys=True, indent=4))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def serialize_instance(obj):
    d = {'__classname__':type(obj).__name__}
    d.update( vars(obj) )
    return d

classes = {
    'Point':Point
}

def unserialize_object(d):
    clsname = d.pop('__classname__',None)
    if clsname:
        cls = classes[ clsname ]
        obj = cls.__new__( cls )
        for key, value in d.items():
            setattr(obj, key, value)
            return obj
    else:
        return d

p = Point(2, 3)
s = json.dumps(p, default=serialize_instance )
print( s )

a = json.loads(s, object_hook=unserialize_object )
print( a )