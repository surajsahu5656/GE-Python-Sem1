#WAP to create a pyramid of the character ‘*’ and a reverse pyramid

def pyramid(n):
    k = n - 1
    for i in range(n):
        for j in range(0, k):
            print(end=" ")
        k -= 1
        for j in range(0, (2 * i) + 1):
            print("*", end='')
        print("\r")

def reverse(m):
    k = 0
    for i in range(m - 1, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k += 1
        for j in range(0, (2 * i) + 1):
            print("*", end='')
        print("\r")

num = int(input("Enter number of rows: "))

pyramid(num)
reverse(num)


#Another ways
n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for k in range(2*i+1):
        print("*",end='') 
    print() 
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(' ',end='')
    for k in range(2*i-1):
        print('*',end="")
    print()    
