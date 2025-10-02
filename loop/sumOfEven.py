# Sum of even numbers from 1 to 100

a = 0

for i in range(0, 101):
    if i%2==0:
        a += i
print("Sum of even numbers from 1 to 100 is", a)