def sum(s):
    if len(s) == 0:
        return 0
    else:
        total = int(s[0]) + int(sum(s[1::]))
        return total


print(sum(str(223)))
