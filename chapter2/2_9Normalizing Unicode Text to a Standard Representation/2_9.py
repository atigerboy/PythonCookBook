s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print( s1, s2 )
print( s2 == s1, len(s1), len(s2) )
import  unicodedata

#.  NFC means that characters should be fully composed
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
#NFD means that characters should be fully decomposed with the use of combining characters.
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)

print( t1 == t2, ascii(t1), ascii(t2))
print( t3 == t4, ascii(t3), ascii(t4))

print( ''.join(c for c in t1 if not unicodedata.combining(c)) )
print( ''.join(c for c in t3 if not unicodedata.combining(c)) )