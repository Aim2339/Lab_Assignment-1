# Find the squareroot of a given number

def root(x):
    return x**(1/2)

num = int(input("Enter a number: "))
print("Squareroot of", num, "is", root(num))