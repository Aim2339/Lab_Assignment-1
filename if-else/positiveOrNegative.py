# Check whether a given number is positive or negative

x = int(input("Enter a number: "))

if x>0:
    print(x," is positive number")
elif x==0:
    print(x, "is neither positive nor negative")
else:
    print(x, "is a negative number")