# if the character is a letter, print whether the letter is uppercase or lowercase

# Input a character from the user
character = input("Enter a character: ")

# Check if the character is a letter
if character.isalpha():
    if character.isupper():
        print(f"{character} is an uppercase letter.")
    elif character.islower():
        print(f"{character} is a lowercase letter.")
else:
    print(f"{character} is not a letter.")
