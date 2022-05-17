from posixpath import split


sRaw = "Hello World"
s = sRaw.split(" ")
newS = ""
for i in s:
    i = i.lower()
    j = sorted(i)
    k = "".join(j)
    newS = newS + k + " "
newS = newS.rstrip()
print(newS)


