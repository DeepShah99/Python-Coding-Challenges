from heapq import merge


dictA = {"a":1, "b":2, "c":3}
dictB = {"d":1, "e":2, "c":4}
#dictC = {**dictA, **dictB}
dictC = dictA | dictB
print(dictC)

