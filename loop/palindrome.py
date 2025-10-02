# Check if a number is a palindrome

y = str(input("Enter a number: "))

if y == y[::-1]:
    print(y, "is a palindrome")
else:
    print(y, "is not a palindrome")