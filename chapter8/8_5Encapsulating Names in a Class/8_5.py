'''
一个下划线(_)开头的代表内部实现
两个下划线(__)代表为类定义，通常为类的默认函数，具有特殊的调用时期
比如__init__, __repr__,__enter__等
这只是约定，但不妨碍直接访问。
'''

class A:
    def __init__(self):
        self._internal = 0 # An internal attribute
        self.public = 1 # A public attribute
    def public_method(self):
        '''
        A public method
        '''
        self._internal_method()
    def _internal_method(self):
        print( self._internal )
        print( self.public )

class B(A):
    def __init__(self):
        super().__init__()
        self._internal = 2 #  override A._internal
        self.public = 3 # override A.public
    def public_method(self):
        '''
        A public method
        '''
        self._internal_method()
    def _internal_method(self):
        super()._internal_method()
        print( vars( self ) )

b = B()
b.public_method()