# Sum of numbers till input is 0

n = float(input("Enter a number (0 to stop): "))
count = 0

while n !=0:
    n = float(input("Enter a number (0 to stop): "))
    count +=n
print("Sum of the numbers entered till now is:",count)


