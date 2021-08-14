CHUNKSIZE = 8192

def readers(s):
    while True:
        data = s.recv( CHUNKSIZE )
        if data == b'':
            break
        #do process data

def readers2(s):
    for chunk in iter( lambda :s.recv(CHUNKSIZE), b''):
        #do process data
        pass