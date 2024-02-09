#if the character is a numeric digit, prints its name in text (e.g., if input is 9, output is NINE)

# Input a character from the user
character = input("Enter a character: ")

# Check if the character is a numeric digit
if character.isdigit() and len(character) == 1:
    digit = int(character)
    digit_names = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    
    if digit >= 0 and digit <= 9:
        print(f"The textual representation of {character} is {digit_names[digit]}.")
    else:
        print("Invalid input. Please enter a single digit (0-9).")
else:
    print(f"{character} is not a numeric digit.")
