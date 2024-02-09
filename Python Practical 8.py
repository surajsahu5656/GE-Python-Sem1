'''WAP to create a list of the cubes of only the even integers appearing in the input list (may have
elements of other types also) using for loop and list comprehension.
'''

#Using a for loop:
def cubes_of_even_numbers_for_loop(input_list):
    result = []
    for item in input_list:
        if isinstance(item, int) and item % 2 == 0:
            result.append(item ** 3)
    return result

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cubes = cubes_of_even_numbers_for_loop(input_list)
print(cubes)

#Using list comprehension:
def cubes_of_even_numbers_list_comprehension(input_list):
    return [item ** 3 for item in input_list if isinstance(item, int) and item % 2 == 0]

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cubes = cubes_of_even_numbers_list_comprehension(input_list)
print(cubes)


