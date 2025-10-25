# Check whether a given number is prime or composite

n = int(input("Enter a number: "))

for i in range(2, int(n**0.5)+1):
    if n%i==0:
        print(n,"is a composite number")
        break
    else:
        print(n,"is a prime number")