# Swap values of two variables

def swap(x, y):
    return y, x

a = float(input("Enter a= "))
b = float(input("Enter b= "))

a, b = swap(a, b)
print("After swap: a=",a, "b=",b)
