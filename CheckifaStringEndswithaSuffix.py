s = "Coding"
suffix = "Coding"
print(s[len(s) - len(suffix)::] == suffix)  # option 1

print(s.endswith(suffix)) #option 2