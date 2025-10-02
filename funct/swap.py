# Swap values of two variables

def swap(x, y):
    return y, x

a = float(input("Enter first number a= "))
b = float(input("Enter second number b= "))

a, b = swap(a, b)
print("After swap: a=",a, "b=",b)
