n = int(input("Enter the number n : "))
fact = 1
for i in range(n,0,-1):
    fact = fact * i
print(fact)