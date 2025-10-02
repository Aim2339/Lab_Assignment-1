# Factorial of a given number

n = int(input("Enter a number: "))
a = 1

for i in range(1, n+1):
    a *= i
print("Factorial of", n, "is", a)