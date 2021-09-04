'''
cyclic data structures( Tree, graphs, Observer Patterns)
using weakref library
似乎完全没用啊
'''
import weakref


class Node:
    def __init__(self,value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return 'Node({!r:})'.format( self.value )

    #property that manages the parent as a weak-reference
    @property
    def parent(self):
        return self._parent if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref( node )

    def add_child(self, child ):
        self.children.append( child )
        child.parent = self

root = Node('parent')
c1 = Node('child')
root.add_child( c1 )
print( c1.parent )
del root
print( c1.parent )#None,delete  Immediately

class Data:
    def __del__(self):
        print('Data.__del__')
# Node class involving a cycle
class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
print('==============new test==================')
import gc
a = Node()
a_ref = weakref.ref( a )
a.add_child(Node())
del a
gc.collect()
print( a_ref )
