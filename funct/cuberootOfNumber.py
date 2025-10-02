# Find the cuberoot of a given number

def root(x):
    return x**(1/3)

num = int(input("Enter a number: "))
print("Cuberoot of", num, "is", root(num))