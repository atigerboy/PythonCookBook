import  pandas

#TODO:: pandas的库的用法跟文档中完全不一样了，详细学了之后再补充
rats = pandas.read_csv( '311_Service_Requests_-_Rodent_Baiting_-_Historical.csv', skipfooter=1,engine='python')
print( rats )