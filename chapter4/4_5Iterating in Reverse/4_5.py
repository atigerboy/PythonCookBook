a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)

class Countdown:
    def __init__(self, start):
        self.start = start
    # Forward iterator
    def __iter__(self):#called by in or iter()
        n = self.start
        while n > 0:
            yield n
            n -= 1
    # Reverse iterator
    def __reversed__(self): #called by reversed()
        n = 1
        while n <= self.start:
            yield n
            n += 1

c = Countdown(5)
for n in c:
    print( n )
for n in reversed( c ):
    print( n )