#WAP to read a file and Copy even lines of the file to a file named ‘File1’ and odd lines to another file named ‘File2’.

def copy_even_and_odd_lines(filename):
    try:
        with open(filename, 'r') as file, open('File1.txt', 'w') as even_file, open('File2.txt', 'w') as odd_file:
            lines = file.readlines()

            for i, line in enumerate(lines):
                if i % 2 == 0:
                    even_file.write(line)
                else:
                    odd_file.write(line)

        print("Even lines copied to 'File1.txt'")
        print("Odd lines copied to 'File2.txt'")

    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    filename = input("Enter the name of the file to copy from: ")
    copy_even_and_odd_lines(filename)
