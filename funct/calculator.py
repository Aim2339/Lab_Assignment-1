# Basic calculator

def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mult(a, b):
    return a*b
def div(a, b):
    return a/b

x = int(input("Enter first number a="))
y = int(input("Enter second number b="))
z = input("Enter operator (+,-,/,*): ")

if z=="+":
    print("a+b", add(x, y))
if z=="-":
    print("a-b", sub(x, y))
elif z=="*":
    print("a*b", mult(x, y))
elif z=="/":
    print("a/b", div(x, y))
else:
    print("Enter a valid operator/number")