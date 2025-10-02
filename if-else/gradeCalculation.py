# Find grade by entering your marks

marks = float(input("Enter your marks (out of 100): "))

if 90 < marks <100:
    print("Grade S")
elif 80 < marks <= 90:
    print("Grade A")
elif 70 < marks <= 80:
    print("Grade B")
elif 50 < marks <= 70:
    print("Grade C")
elif 0<= marks <= 50:
    print("Grade D")
else:
    print("Enter valid marks between 0 to 100")