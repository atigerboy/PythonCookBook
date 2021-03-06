'''
Header:
Byte Type Description
0 int File code (0x1234, little endian)
4 double Minimum x (little endian)
12 double Minimum y (little endian)
20 double Maximum x (little endian)
28 double Maximum y (little endian)
36 int Number of polygons (little endian)

Record:
Byte Type Description
0 int Record length including length (N bytes)
4-N Points Pairs of (X,Y) coords as doubles

看上去只能一行一行的解析了
'''

import struct
import itertools

polys = [
[ (1.0, 2.5), (3.5, 4.0), (2.5, 1.5) ],
[ (7.0, 1.2), (5.1, 3.0), (0.5, 7.5), (0.8, 9.0) ],
[ (3.4, 6.3), (1.2, 0.5), (4.6, 9.2) ],
]

def write_polys(filename, polys):
    #Determine bounding box
    flattend = list( itertools.chain( *polys ))
    min_x = min( x for  x,y in flattend )
    max_x = max( x for x, y in flattend )
    min_y = min( y for x, y in flattend )
    max_y = max( y for x, y in flattend )
    with open( filename, 'wb' ) as f:
        f.write(struct.pack('<iddddi',
                            0x1234,
                            min_x, min_y,
                            max_x, max_y,
                            len(polys)
        ))
        for poly in polys:
            size = len(poly) * struct.calcsize('<dd')
            f.write(struct.pack('<i', size+4))
            for pt in poly:
                f.write( struct.pack('<dd', *pt))

write_polys('polys.bin', polys )

## 太多magic number了 自说明性较差，当格式变更的时候需要重新手动计算数值
def read_polys(filename):
    with open(filename, 'rb') as f:
        # Read the header
        header = f.read(40)
        file_code, min_x, min_y, max_x, max_y, num_polys = \
        struct.unpack('<iddddi', header)
        polys = []
        for n in range(num_polys):
            pbytes, = struct.unpack('<i', f.read(4))
            poly = []
            for m in range(pbytes // 16):
                pt = struct.unpack('<dd', f.read(16))
                poly.append(pt)
            polys.append(poly)
    return polys

print( read_polys( 'polys.bin' ) )

class StructField:
    ''' Descriptor representing a simple structure field'''
    def __init__(self , format, offset):
        self.format = format
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            r = struct.unpack_from(self.format, instance._buffer, self.offset)
            return r[0] if len(r) == 1 else r

class NestedStruct:
    '''Descriptor reprsenting a nested structure'''
    def __init__(self, name, struct_type, offset):
        self.name = name
        self.struct_type = struct_type
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            data = instance._buffer[self.offset:self.offset + self.struct_type.struct_size]
            result = self.struct_type( data )
            #Save resulting structure back on instance to avoid
            #further recomputation of this step
            setattr(instance, self.name, result)
            return result


class StructureMeta( type ):
    '''Metaclass that automatically creates StructField descriptor'''
    def __init__(self, clsname, bases, clsdict):
        fields = getattr( self, '_fields_',[])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if isinstance( format, StructureMeta):
                setattr( self, fieldname, NestedStruct(fieldname, format, offset))
                offset += format.struct_size
            else:
                if format.startswith(('<','>','!','@')):
                    byte_order=format[0]
                    format = format[1:]
                format = byte_order+format
                setattr( self, fieldname, StructField(format, offset))
                offset += struct.calcsize(format)
        setattr(self, 'struct_size', offset )

class Structure(metaclass=StructureMeta):
    def __init__(self, bytedata ):
        self._buffer = memoryview( bytedata )

    @classmethod
    def from_file(cls, f):
        return cls(f.read(cls.struct_size))

class PolyHeader( Structure ):
    _fields_ = [
        ('<i', 'file_code'),
        ('d', 'min_x'),
        ('d', 'min_y'),
        ('d', 'max_x'),
        ('d', 'max_y'),
        ('i', 'num_polys')
    ]

f = open( 'polys.bin','rb')
phead = PolyHeader.from_file(f)
print( phead.file_code == 0x1234 )
print( phead.num_polys  )
f.close()

class Point( Structure ):
    _fields_= [
        ('<d','x'),
        ('d','y')
    ]

class PolyHeadNest( Structure ):
    _fields_ = [
        ('<i', 'file_code'),
        (Point, 'min'),  # nested struct
        (Point, 'max'),  # nested struct
        ('i', 'num_polys')
    ]
f = open( 'polys.bin','rb')
phead = PolyHeadNest.from_file(f)
print( phead.file_code == 0x1234 )
print( phead.min )
print( phead.max )
print( phead.num_polys  )
f.close()

class SizedRecord:
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)
    @classmethod
    def from_file(cls, f, size_fmt, includes_size=True):
        sz_nbytes = struct.calcsize(size_fmt)
        sz_bytes = f.read(sz_nbytes)
        sz, = struct.unpack(size_fmt, sz_bytes)
        buf = f.read(sz - includes_size * sz_nbytes)
        return cls(buf)
    def iter_as(self, code):
        if isinstance(code, str):
            s = struct.Struct(code)
            for off in range(0, len(self._buffer), s.size):
                yield s.unpack_from(self._buffer, off)
        elif isinstance(code, StructureMeta):
            size = code.struct_size
            for off in range(0, len(self._buffer), size):
                data = self._buffer[off:off+size]
                yield code(data)


f = open('polys.bin', 'rb')
phead = PolyHeader.from_file(f)
print( phead.num_polys )
polydata = [ SizedRecord.from_file(f, '<i') for n in range( phead.num_polys )]
print( polydata )

for n, poly in enumerate( polydata ):
    print( 'Polygon', n )
    for p in poly.iter_as( '<dd'):
        print( p )