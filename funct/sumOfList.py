# Find the total sum of numbers in a list

def listsum(li):
    total = 0

    for i in li:
        total += i
    return total

x = [1, 0.1, 4, 5.3, 6.9, 10]

print("Sum of the numbers in the list is:", listsum(x))