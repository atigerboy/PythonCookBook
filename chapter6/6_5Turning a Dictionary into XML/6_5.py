from xml.etree.ElementTree import Element

def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into xml
    '''
    elem = Element(tag)
    for key,val in d.items():
        child = Element( key )
        child.text = str(val)
        elem.append( child )
    return elem

s = { 'name': 'GOOG', 'shares': 100, 'price':490.1 }
e = dict_to_xml('stock', s)

from xml.etree.ElementTree import tostring
print( tostring(e) )

def dict_to_xml_str( tag, d ):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    parts = ['<{}>'.format(tag)]
    for key, val in d.items():
        parts.append('<{0}>{1}</{0}>'.format(key, val))
    parts.append('</{}>'.format(tag))
    return ''.join(parts)

print( dict_to_xml_str('stack', s) )