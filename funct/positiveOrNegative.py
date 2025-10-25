# Check whether a given number is positive or negative

def sign(x):
    if x > 0:
        print(x, "is positive number")
    elif x == 0:
        print(x, "is neither positive nor negative")
    else:
        print(x, "is a negative number")

y = int(input("Enter a number: "))
sign(y)