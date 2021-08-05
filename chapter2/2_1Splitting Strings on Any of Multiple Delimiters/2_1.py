# -*- coding: utf-8 -*-

line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
#separator is comma(,) or semicolon(;) or whitespace( ) followed by any amount of extra whitespace
segments = re.split(r'[;,\s]\s*',line)
print( segments )
#() in pattern means capture group.if capture groups are used,then the matched text is also included in the result
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
values = fields[::2]
delimiters = fields[1::2] + [' ']
print(values)
print(delimiters)

#Reform the line using the same delimiters
print(''.join(v+d for v,d in zip(values, delimiters)))

"""
If you don’t want the separator characters in the result, but still need to use parentheses
to group parts of the regular expression pattern, make sure you use a noncapture group,
specified as  (?:...)
"""
print( re.split(r'(?:,|;|\s)\s*', line) )


