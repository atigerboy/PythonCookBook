def avg( first, *rest):#*for tuple 必须放最后
    return (first + sum(rest)) /(1+len(rest))

print( avg(1,2) )
print( avg(1,2,3))

import html

def make_element( name, value, **attrs ):#** for dict 必须放最后
    keyvals =[' %s="%s"' % item for item in attrs.items() ]
    attr_str = ''.join( keyvals )
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name = name,
        attrs = attr_str,
        value = html.escape(value)
    )
    return element

print( make_element( 'item','Albatross', size='large',quantity=6 ))
print( make_element( 'p','<spam>'))

def anyargs(*args, **kwargs):#order
    print( args )
    print( kwargs )