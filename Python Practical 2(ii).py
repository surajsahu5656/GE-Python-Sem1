# Generate all prime numbers till ‘n’

n=int(input('enter an integer:-'))         
if n<2:
      print('enter a valid number')
else:       
    for num in range(2,n+1):
            if all(num%i!=0 for i in range(2,num)):
                print(num)
