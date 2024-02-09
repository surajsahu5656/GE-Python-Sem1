# To check if the number is prime or not

n=int(input('enter an integer'))
if n<2:
    print(n,' is not an prime number')
else:
        if any(n%i==0 for i in range(2,n)):
            print(n, 'is not an prime number')
        else:
            print(n,'is a prime number')   

