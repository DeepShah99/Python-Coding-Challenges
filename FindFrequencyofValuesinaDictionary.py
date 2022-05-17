from itertools import count
my_dict = {
	"a": 4,
	"b": 4,
	"c": 2,
	"d": 7,
	"e": 4,
	"f": 2,
	"g": 7,
	"h": 7
 }
#my_dict = {}
freq_dict = {}

if my_dict == {}:
    print(freq_dict)
else:
    rawList = []
    for i in my_dict.values():
        rawList.append(i)
    #print(rawList)
    for i in rawList:
        if i not in freq_dict:
            freq_dict[i] = rawList.count(i)
    print(freq_dict)