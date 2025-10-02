#Sum of n numbers

n = int(input("Enter a number: "))
a = 0

for i in range(0, n+1):
    a += i
print("Sum of numbers from 0 to", n, "is", a)
