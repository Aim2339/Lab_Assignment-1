# Fibonacci series for n terms

n = int(input("Enter a term number: "))
a=0;b=1

for i in range(n):
    print(a)
    a,b = b, a+b

