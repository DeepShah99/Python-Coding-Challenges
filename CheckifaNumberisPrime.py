num = int(input("Enter a number: "))
prime = True
if num == 0 or num == 1:
    prime = False
for i in range(2,num):
    if num % i == 0:
        prime = False
        break
if prime:
    print("Prime")
else:
    print("Not prime")