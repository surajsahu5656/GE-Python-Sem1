#Replace a character by another character in a string.

# Input a string from the user
text = input("Enter a string: ")

# Input the character to replace
char_to_replace = input("Enter the character to be replaced: ")

# Input the character to replace with
replacement_char = input("Enter the character to replace with: ")

# Use the replace() method to replace all occurrences of the character
modified_text = text.replace(char_to_replace, replacement_char)

# Display the modified string
print(f"The modified string: {modified_text}")


#Another way
'''def replacd_old_chr(s,old_chr,new_chr):
    return(s.replace(old_chr,new_chr))

#eg.
print(replacd_old_chr('this is awesome',"that","this"))'''