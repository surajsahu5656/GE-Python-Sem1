#WAP to read a file and Print the words in reverse order.

def reverse_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                reversed_words = [word[::-1] for word in words]  # Reverse each word
                reversed_line = ' '.join(reversed_words)
                print(reversed_line)

    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    filename = input("Enter the name of the file: ")
    reverse_words_in_file(filename)
