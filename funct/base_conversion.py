def base_conversion(num):
    return {
        "binary": bin(num),
        "octal": oct(num),
        "hexadecimal": hex(num)
    }
n = int(input("Enter a number: "))
print("Base conversion of",n,"is",base_conversion(n))