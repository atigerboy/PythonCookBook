'''
You want to implement a custom class that mimics the behavior of a common built-in
container type, such as a list or dictionary. However, you’re not entirely sure what
methods need to be implemented to do it.
'''

from collections import  abc
import  collections
import bisect

'''Implement Containers only implement some methods, not all you used'''
class SortedItems( abc.Sequence ):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial  else []

    #Required sequence methods
    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    #Method for adding an item in the right location
    def add(self , item ):
        bisect.insort( self._items, item )

items = SortedItems([5,1,3,7])
print( list( items ))
print( items[0] )
print( items[-1] )
items.add(2)
print( 2 in items )