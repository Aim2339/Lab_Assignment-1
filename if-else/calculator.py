# Basic calculator

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = str(input("Enter operator (+,-,/,*): "))
if z=="+":
    print(x+y)
elif z== "-":
    print(x-y)
elif z=="/":
    print(x/y)
elif z=="*":
    print(x*y)
else:
    print("Not correct operator")