#WAP to swap the first n characters of two strings.

# Input two strings from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Input the number of characters to swap
n = int(input("Enter the number of characters to swap: "))

# Check if the length of both strings is at least n
if len(string1) >= n and len(string2) >= n:
    # Swap the first n characters by creating two new strings
    swapped_string1 = string2[:n] + string1[n:]
    swapped_string2 = string1[:n] + string2[n:]
    
    print(f"Swapped string 1: {swapped_string1}")
    print(f"Swapped string 2: {swapped_string2}")
else:
    print("Both strings should have at least n characters to perform the swap.")
