'''Write a function that accepts two strings and returns the indices of all the occurrences of the
second string in the first string as a list. If the second string is not present in the first string then it
should return -1.'''

def find_all_occurrences(main_string, sub_string):
    if sub_string not in main_string:
        return -1
    
    indices = []
    start = 0
    while True:
        index = main_string.find(sub_string, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1 

    return indices

main_string = input("Enter the first string: ")
sub_string = input("Enter the second string: ")
result = find_all_occurrences(main_string, sub_string)
if result != -1:
    print(f"The '{sub_string}' substring occurs at indices: {result}")
else:
    print(f"The '{sub_string}' substring was not found.")


#Another way
'''l=[]
str1=input('enter value:-')
str2=input('enter another string:-')
for i in str1:
    if i in str2:
        k=str1.index(i)
        l.append(k)
print(l)     
'''
