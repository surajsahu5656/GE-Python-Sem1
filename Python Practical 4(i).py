# print whether the character is a letter or numeric digit or a special character

# Input a character from the user
character = input("Enter a character: ")

# Check if the character is a letter
if character.isalpha():
    print(f"{character} is a letter.")
    
# Check if the character is a numeric digit
elif character.isdigit():
    print(f"{character} is a numeric digit.")
    
# If it's not a letter or a numeric digit, consider it a special character
else:
    print(f"{character} is a special character.")
