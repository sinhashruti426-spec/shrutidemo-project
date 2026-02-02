# check if a number is prime:
n=int(input("enter a number: "))
if(n//n==1 and n//1==n):
    print(n,"is prime number")
else:
    print(n,"is not prime number")


# find a factorial of a number(loop):
n=int(input("enter a number: "))
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i+=1
