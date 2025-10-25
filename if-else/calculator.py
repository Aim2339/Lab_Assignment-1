# Basic calculator

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = str(input("Enter operator (+,-,/,*): "))

if z=="+":
    print("a+b=", x+y)
if z=="-":
    print("a-b=", x-y)
elif z=="*":
    print("a*b=", x*y)
elif z=="/":
    print("a/b=", x/y)
else:
    print("Enter a valid operator/number")