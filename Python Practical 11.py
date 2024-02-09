'''Write a function that prints a dictionary where the keys are numbers between 1 and 5 and the
values are cubes of the keys.'''

def print_cubed_dictionary():
    cubed_dict = {key: key**3 for key in range(1, 6)}

    for key, value in cubed_dict.items():
        print(f"Key: {key}, Cube: {value}")

print_cubed_dictionary()
def print_cubed_dictionary():
    cubed_dict = {key: key**3 for key in range(1, 6)}

    for key, value in cubed_dict.items():
        print(f"Key: {key}, Cube: {value}")

print_cubed_dictionary()
