class Person:
    def __init__(self, name):
        self.name = name
    # Getter function
    @property
    def name(self):
        return self._name
    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value
    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson( Person ):
    pass

s = SubPerson('Guido')
print( s.name )
s.name = 'Larry'
print( s.name )
try:
    s.name = 42
except TypeError as e:
    print(e)

class SubPerson2( Person ):
    @Person.name.getter
    def name(self):#not call,why??
        print('Getting name',end='')
        return super(SubPerson2, SubPerson2).name.__get__(self)
    @Person.name.setter
    def name(self,value):
        print('setting name to ', value )
        super(SubPerson2, SubPerson2).name.__set__(self, value)

s = SubPerson2('Guido')
print( s.name )
s.name ='Larry'
print( s.name )

