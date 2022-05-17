my_dict = {
	"a": [1, 2, 3],
	"b": [4, 0, -4],
	"c": [3, 5, 9],
	"d": [45, 12, 100]
}
max = None
for i in my_dict.values():
        temp = sum(i)
        if max == None:
            max = temp
        if temp > max:
            max = temp
print(max) 
   
