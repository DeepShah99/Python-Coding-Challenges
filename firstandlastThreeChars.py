s = "Wonderful"
if(len(s) >= 6):
   result =  s[:3:]
   result = result + s[len(s) - 3::]
   print(result)
else:
    print("")