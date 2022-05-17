def convert_binary(n):
    if n == 0:
        return "0"
    else:
        return (convert_binary(n//2) + str(n%2)).lstrip("0")

print(convert_binary(5))