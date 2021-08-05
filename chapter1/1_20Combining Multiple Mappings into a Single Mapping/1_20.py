a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

#从后面的例子来看 ChainMap的使用会让人有迷惑的地方 还是自己写代码合并吧。
from collections import ChainMap
c = ChainMap(a, b)
print(list(c.keys()))
print(list(c.values()))
c['z'] = 10
c['w'] = 40
print(list(c.items()))
del c['x']
print(a)
try:
    del c['y']#key not found in the first mapping
except Exception as err:
    print( err )
