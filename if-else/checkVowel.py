# Check if a given letter is vowel or consonant

vowel = ["a", "e", "i", "o", "u"]
consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

letter = input("Enter a letter: ").lower()

if letter in vowel:
    print(letter, "is a vowel")
elif letter in consonant:
    print(letter, "is a consonant")
else:
    print("Couldn't determine whether given letter is a vowel or consonant")