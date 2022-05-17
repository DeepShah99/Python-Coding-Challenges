A = [1,2,3,4]
A.sort(reverse=True)
if A == [] or len(A) == 1:
    print(None)
else: 
    print(A[len(A)-2])