def pattern(n):
    if n == 1:
        return "*"
    else:
        print("*" * n)
        return pattern(n - 1)

print(pattern(6))