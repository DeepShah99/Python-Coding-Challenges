s = "Corporation"
tempset = set()
repeat = 0
count = 1
data = ""
for i in s:
    for j in range (count, len(s)):
        if i == s[j]:
         tempset.add(i)
    count+=1
tempset = sorted(tempset)
for i in tempset:
    data = data + i + " "
if tempset == []:
    print("0")
else:
    print(len(tempset))
if data == "":
    print("None")
else:
    print(data)

