#Remove all occurrences of a character from a string.

# Input a string from the user
text = input("Enter a string: ")

# Input the character to remove
char_to_remove = input("Enter the character to remove: ")

# Initialize an empty string to store the modified string
modified_text = ""

# Iterate through the original string and exclude the specified character
for char in text:
    if char != char_to_remove:
        modified_text += char

# Display the modified string without the specified character
print(f"The modified string: {modified_text}")


#Another way
'''def remove_all_occurenc_of_chr(s,chr):
    return(s.replace(chr,''))

#eg.
print(remove_all_occurenc_of_chr("what do you mean? i am starboy rolling on my own deep ","o"))
'''