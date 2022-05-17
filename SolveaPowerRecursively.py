def pow(a,n):
    if n == 0:
        return 1
    else:
        total = a * pow(a,n-1)
        return total

print(pow(2,0))