s = "ABCD"
n = 3
if s == "" or len(s) < n:
    print(s)
else:
    result = s[:n:]
    result = result + s[n+1::] 
    print(result)