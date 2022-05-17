from math import gcd
def two_gcd(a,b):
    if b == 0:
        return a
    else:
        return two_gcd(b, a%b)

print(two_gcd(12,24))
    
print(12%24)