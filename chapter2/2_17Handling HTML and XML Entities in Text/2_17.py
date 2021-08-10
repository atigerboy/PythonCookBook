s = 'Elements are written as "<tag>text</tag>".'
print(s)
import html
print( html.escape( s ))
print( html.escape(s, quote=False))
s0 = 'Spicy Jalapeño'
print( s0.encode('ascii', errors='xmlcharrefreplace'))

s1 = 'Spicy &quot;Jalape&#241;o&quot.'
print( html.unescape( s1 ))
print( html.escape( s0 ))
print( html.unescape( html.escape(s0 )), s0)