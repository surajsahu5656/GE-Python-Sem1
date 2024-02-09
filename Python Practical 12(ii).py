'''' Consider a tuple t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10).
WAP to Print another tuple whose values are even numbers in the given tuple.'''

t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# Create a new tuple containing even numbers from t1
even_numbers = tuple(x for x in t1 if x % 2 == 0)

# Print the tuple of even numbers
print("Tuple of even numbers:", even_numbers)
