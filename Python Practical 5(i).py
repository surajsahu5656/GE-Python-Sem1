#Find the frequency of a character in a string.

# Input a string from the user
text = input("Enter a string: ")

# Input the character to find its frequency
char_to_find = input("Enter the character to find its frequency: ")

# Initialize a variable to store the frequency count
frequency = 0

# Iterate through the string to count the frequency of the character
for char in text:
    if char == char_to_find:
        frequency += 1

# Display the frequency of the character
print(f"The frequency of '{char_to_find}' in the string is: {frequency}")


#Another Way
'''def count(s,chr):
    return(s.count(chr))

#eg.
print(count('on my own','o'))'''
