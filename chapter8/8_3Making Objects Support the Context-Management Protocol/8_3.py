'''context-mamagement protocol( the with statement)
you need to implement __enter__() and __exit__() methods
'''
from socket import socket, AF_INET, SOCK_STREAM
class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.sock = None
    def __enter__(self): #enter context
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock
    def __exit__(self, exc_ty, exc_val, tb):#exit context for clean up
        self.sock.close()
        self.sock = None

from functools import partial
conn = LazyConnection(('www.python.org', 80))
# Connection closed
with conn as s:
    # conn.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    print( resp )

#注意如何处理嵌套with的问题
from socket import socket, AF_INET, SOCK_STREAM
class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.connections = []#Pool for connections

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock) #in cache
        return sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()

from functools import partial
conn = LazyConnection(('www.python.org', 80))
# Connection closed
with conn as s:
    # conn.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    print( resp )
    with conn as s2: #s1 and s2 are independent sockets
        # conn.__enter__() executes: connection open
        s2.send(b'GET /index.html HTTP/1.0\r\n')
        s2.send(b'Host: www.python.org\r\n')
        s2.send(b'\r\n')
        resp = b''.join(iter(partial(s2.recv, 8192), b''))
        print(resp)