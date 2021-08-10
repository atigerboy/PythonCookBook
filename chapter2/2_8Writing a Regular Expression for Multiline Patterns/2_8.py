import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
            multiline comment */
'''
print( comment.findall( text1 ))
print( comment.findall(( text2 )))

# (?:.|\n) specifies a noncapture group for .(any character not newline) \n new line)
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print( comment.findall( text2 ))

#use flage re.DOTALL make . in regular expression match all characters, including newlines.(no good)
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print( comment.findall( text2 ))