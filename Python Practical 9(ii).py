#WAP to read a file and Calculate the frequency of each character in the file. Use a variable of dictionary type to maintain the count.

def count_character_frequency(filename):
    character_frequency = {}

    try:
        # Open the file for reading
        with open(filename, 'r') as file:
            for line in file:
                # Iterate through each character in the line
                for char in line:
                    if char.isalnum():
                        # If the character is alphanumeric (letters or numbers)
                        # Increment its count in the dictionary
                        char = char.lower()  # Consider characters in a case-insensitive manner
                        if char in character_frequency:
                            character_frequency[char] += 1
                        else:
                            character_frequency[char] = 1

        # Print the character frequency count
        for char, count in character_frequency.items():
            print(f"'{char}' appears {count} times.")

    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    filename = input("Enter the name of the file: ")
    count_character_frequency(filename)
