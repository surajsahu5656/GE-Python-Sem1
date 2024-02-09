''' Consider a tuple t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10).
WAP to Print half the values of the tuple in one line and the other half in the next line.'''

t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# Calculate the midpoint to split the tuple
midpoint = len(t1) // 2

# Print the first half
print("First Half:")
for value in t1[:midpoint]:
    print(value, end=" ")

# Print a new line
print()

# Print the second half
print("Second Half:")
for value in t1[midpoint:]:
    print(value, end=" ")
