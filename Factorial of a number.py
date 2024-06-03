#finding a factorial 
n=int(input("Enter the number: "))
factorial=1
if n<0:
    print("The number you have entered in negative")
elif n==0:
    print("Factorial is",n)
else:
    for i in range(1,n+1):
        factorial*=i
    print("The factorial of",n,"is",factorial)
