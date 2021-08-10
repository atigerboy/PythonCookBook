# PythonCookBook
## 1 Data Structures and Algorithms 总结
1. unpack iterator的几个方式 有关的问题有1——1，1——2，1——18
	name list = iterator 其中 当variable 跟iterator的数量匹配是 一一对应，如果出现数量不确定是 可以用\* variable 来匹配任意多的elements，当不关心的内容 可以用特殊字符 _ 或者 \*\_ 来匹配，特殊字符的好处是在variable name list中可以出现多次。namedtuple的优点是匹配类似dataset型的数据时能够定义一个struct，然后将数据填充，但是这里没有\* variable的形式，另外，比如 a,\*b=range(1,10),此时a，b就会展开成list了。
2. dictionary的本身操作，有关问题有1——6，1——7，1——9，1——13，1——14
	常规操作有 dictionary 单key对应多value 此时用defaultdict(list),defaultdict(set).有序dictionary可以用OrderedDict(),默认用key的字典序来排。dictionary的并|交操作，这里主要是根据dict.keys()支持&操作以及-操作 那么并操作等于 a-b + b即可，用ChainMap非常不好用，不推荐。排序使用的内置函数为sorted 第一个参数为所有的iterator，key可以设置成单个或者tuple。sorted这个内置函数是重点。
3. filter以及类似的操作
   
    

