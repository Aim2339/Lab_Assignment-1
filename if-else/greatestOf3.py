# Find greatest of 3 given numbers

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))

if x>y and x>z:
    print(x, "is the largest number")
elif y>x and y>z:
    print(y, "is the largest number")
elif z>y and z>x:
    print(z, 'is the largest number')
else:
    print("Couldn't determine greatest of the given numbers")