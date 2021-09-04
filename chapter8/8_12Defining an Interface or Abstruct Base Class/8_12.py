''' ABCMeta, abstractmethod property'''
from abc import ABCMeta, abstractmethod
from collections import  abc
class IStream( metaclass=ABCMeta ):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass
    @abstractmethod
    def write(self, data):
        pass

import io

#Register the built-in I/O classes as supporting our interface
IStream.register( io.IOBase )

with  open( 'foo.txt','wt' ) as f:
    print( isinstance( f, IStream ) )#True

from decimal import Decimal
import numbers

x = Decimal('3.4')
print( isinstance( x, numbers.Real ))#False

x =[]

print( isinstance(x, abc.Sequence) )#True
print( isinstance(x, abc.Iterable) )#True
print( isinstance(x, abc.Sized) ) #True
print( isinstance(x, abc.Mapping) ) #False