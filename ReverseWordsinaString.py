from unittest import result


s = "Python is Awesome"
splitString = s.split()
result = ""
for i in range(0,len(splitString)):
    temp = splitString[i]
    reversedWord = temp[::-1]
    result = result + reversedWord + " "

print(result.swapcase())

