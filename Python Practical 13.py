''' WAP to accept a name from a user. Raise and handle appropriate exception(s) if the text entered
by the user contains digits and/or special characters.'''

import string

def is_valid_name(name):
    # Check if the name contains only alphabetic characters and spaces
    valid_chars = set(string.ascii_letters + ' ')
    return all(char in valid_chars for char in name)

try:
    user_name = input("Enter your name: ")
    if not user_name:
        raise ValueError("Name cannot be empty.")
    
    if is_valid_name(user_name):
        print("Name entered:", user_name)
    else:
        raise ValueError("Name contains invalid characters.")
    
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
