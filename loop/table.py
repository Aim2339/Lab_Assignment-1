# Multiplication table of a given number

n = int(input("Enter a number: "))

for i in range(0, 11):
    x = i*n
    print(n,"x",i,"=",x)