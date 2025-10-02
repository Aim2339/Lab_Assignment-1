# Sum of numbers till input is 0

x = float(input("Enter a number (0 to stop): "))
count = 0

while x !=0:
    x = float(input("Enter a number (0 to stop): "))
    count +=x
print("Sum of the numbers entered till now is:",count)


