# Identify the type of triangle

x = float(input("Enter length of 1st side of triangle: "))
y = float(input("Enter length of 2nd side of triangle: "))
z = float(input("Enter length of 3rd side of triangle: "))

if x==y==z:
    print("The triangle is equilateral")
elif x==y or x==z or y==z:
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")