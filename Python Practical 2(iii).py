#Generate first ‘n’ prime numbers

n = int(input("Enter the value of n: "))
l=[]
num=2
while len(l)<=n-1:
    if all(num%i!=0 for i in range(2,num)):
        l.append(num)
    num+=1
print(l)       

