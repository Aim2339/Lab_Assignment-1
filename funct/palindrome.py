# Check if a number/string is a palindrome

def pal(x):
    y = str(x)

    if y==y[::-1]:
        print(y,"is a palindrome")
    else:
        print(y,"is not a palindrome")

z = str(input("Enter something: "))
pal(z)
