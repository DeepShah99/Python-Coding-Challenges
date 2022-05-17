from sys import prefix


s = "sdad"
prefix = "sd"
counter = 0
result = False
if len(prefix) <= len(s):
    for i in prefix:
       if i == s[counter]:
        result = True
        counter += 1
       else:
        result = False
        break
print(result)     #option 1

print(s.startswith(prefix))  #option 2

print(s[:len(prefix)] == prefix)    #option 3