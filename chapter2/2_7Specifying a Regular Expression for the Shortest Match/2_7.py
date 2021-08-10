import re

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print( text1, str_pat.findall( text1 ))

text2 = 'Computer says "no." Phone says "yes."'
print( text2, str_pat.findall(text2))

#However, the  * operator in a regular expression is greedy, so matching is based
#on finding the longest possible match
#To fix this, add the  ? modifier after the  * operator in the pattern

str_pat = re.compile(r'\"(.*?)\"')
print( text2, str_pat.findall(text2))
#In a pattern, the dot matches any character except a newline.
#  Adding the  ? right after operators such
#  as  * or  + forces the matching algorithm to look for the shortest possible match instead.