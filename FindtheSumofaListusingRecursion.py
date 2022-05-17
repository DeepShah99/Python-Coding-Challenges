myList = [1,2,3,4]
def getSum(s):
    if len(s) == 0:
        return 0
    else:
        sumRec = s[0] + getSum(s[1::])
        return sumRec

print(getSum(myList))