# Check if a given year is a leap year

def leap(x):
    if x%4 == 0:
        print(x,"is a leap year")
    else:
        print(x, "is not a leap year")

year = int(input("Enter a year: "))
leap(year)

