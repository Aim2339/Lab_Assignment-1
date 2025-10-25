# Number of vowels in a given text

text = "VIT Bhopal University"
vowels = ["a", "e", "i", "o", "u"]
count = 0

text2 = text.lower()

for i in text2:
    if i in vowels:
        count +=1
print("Total number of vowels in the given string is:",count)

