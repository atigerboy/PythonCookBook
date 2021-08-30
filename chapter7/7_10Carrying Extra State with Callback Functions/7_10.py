def apply_async(func, args,*, callback):
    result = func( *args )
    callback( result )

def print_result(result):
    print('Got:',result)

def add( x, y):
    return x + y

apply_async( add, (2,3), callback=print_result )
apply_async( add, ('hello', 'world'), callback=print_result )

'''
#only 1 function class
class ResultHandler:
    def __init__(self):
        self.sequence = 0
    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))
'''

def make_handler(): #best choice
    sequence = 0
    def handler( result):
        nonlocal  sequence #capturing
        sequence += 1
        print('[{}] Got:{}'.format(sequence, result ))
    return handler

handler = make_handler()
apply_async( add, (2,3) , callback=handler)
apply_async( add, ('hello', 'world'), callback=handler )

#coroutine same as function
def make_handler_coroutine():
    sequence = 0
    while True:
        result = yield #奇怪的语法
        sequence += 1
        print('[{}] Got:{}'.format(sequence, result ))

handler = make_handler_coroutine()
next( handler ) #Advance to the yield
apply_async( add, (2,3) , callback=handler.send)
apply_async( add, ('hello', 'world'), callback=handler.send )