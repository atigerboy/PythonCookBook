'''__repr__ 与__str__的定义与被调用不同点'''
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)
    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

p = Pair(3,4)

print( p )
print('p is {0!r}'.format( p ))#!r for __repr__
print('p is {0}'.format( p ))

