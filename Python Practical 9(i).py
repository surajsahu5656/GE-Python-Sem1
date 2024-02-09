#WAP to read a file and Print the total number of characters, words and lines in the file.

def count_chars_words_lines(filename):
    # Initialize counters
    char_count = 0
    word_count = 0
    line_count = 0

    try:
        # Open the file for reading
        with open(filename, 'r') as file:
            for line in file:
                # Count lines
                line_count += 1

                # Count characters
                char_count += len(line)

                # Split the line into words and count words
                words = line.split()
                word_count += len(words)

        # Print the results
        print(f"Total characters: {char_count}")
        print(f"Total words: {word_count}")
        print(f"Total lines: {line_count}")

    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    filename = input("Enter the name of the file: ")
    count_chars_words_lines(filename)
