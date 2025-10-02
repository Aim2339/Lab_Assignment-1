# Check whether a given number is prime or composite

x = int(input("Enter a number: "))
a = 2

while a <= x/2:
    if x%a==0:
        print(x,"is a composite number")
        break
    a += 1
else:
    print(x,"is a prime number")