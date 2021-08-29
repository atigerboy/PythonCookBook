from collections import namedtuple
from struct import Struct

def write_records(records, format, f):
    '''
    Write a sequence of tuples to a binary file of structures.
    :param records:
    :param format:
    :param f:
    :return:
    '''
    record_struct = Struct(format)
    for r in records:
        f.write( record_struct.pack(*r) )

def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter( lambda: f.read(record_struct.size),b'')
    return  (record_struct.unpack(chunk) for chunk in chunks )

Record = namedtuple( 'Record',['kind','x','y'])

def unpack_records(format, data):
    ''' 返回的是个generator '''
    record_struct = Struct( format )
    return (Record(*record_struct.unpack_from(data, offset)) for offset in range(0, len(data), record_struct.size))

if __name__ == '__main__':
    records = [(1, 2.3, 4.5),
               (6, 7.8, 9.0),
               (12, 13.4, 56.7)]
    with open('data.b','wb') as f:
        write_records( records , '<idd', f)

    restore_data=[]
    with open('data.b', 'rb') as f:
        for rec in read_records('<idd', f):
            restore_data.append( rec )
    print( restore_data )

    restore_data.clear()
    with open('data.b', 'rb') as f:
        data = f.read()
        for r in  unpack_records('<idd',data):
            restore_data.append( r )

    print( restore_data )

    import numpy as np
    f = open('data.b','rb')
    records = np.fromfile(f, dtype='<i,<d,<d')
    print( records )
    print( records[0] )


