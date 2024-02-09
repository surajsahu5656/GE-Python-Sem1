#Remove the first occurrence of a character from a string.

# Input a string from the user
text = input("Enter a string: ")

# Input the character to remove
char_to_remove = input("Enter the character to remove: ")

# Find the index of the first occurrence of the character
index = text.find(char_to_remove)

# Check if the character was found
if index != -1:
    # Remove the character by creating a new string
    modified_text = text[:index] + text[index+1:]
    print(f"The modified string: {modified_text}")
else:
    print(f"The character '{char_to_remove}' was not found in the string.")


#Another way
'''def replace_first_frequency_chr(s,chr):
    return(s.replace(chr,'',1))

#eg.
print(replace_first_frequency_chr("black friday","a"))
'''