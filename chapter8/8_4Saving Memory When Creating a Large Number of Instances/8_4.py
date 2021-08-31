'''
When you define  __slots__ , Python uses a much more compact internal representation
for instances. Instead of each instance consisting of a dictionary, instances are built
around a small fixed-sized array, much like a tuple or list.

A common misperception of  __slots__ is that it is an encapsulation tool that prevents
users from adding new attributes to instances. Although this is a side effect of using
slots, this was never the original purpose. Instead,  __slots__ was always intended to
be an optimization tool.

'''
class Date:
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

