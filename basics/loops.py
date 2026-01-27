# print numbers from 1 to 100
count=1
while count<=100:
    print(count)
    count+=1


# print 100 to 1
i=100
while i>=1: #stopping value
    print(i)
    i-=1


# print the multiplication of number n
n=1098
i=1
while i<=10:
    print(n*i)
    i+=1

""" print the elements of the following lists using a loop
 [1,4,9,16,25,36,49,64,81,100]"""
i=1
n=1
while n<=100:
    print(n)
    i+=2
    n+=i
    


# search for a number X in this tuple using loop
t=(1,4,9,16,25,36,49,81,100)
i=0
x=36
while i<len(t):
    if(t[i]==x):
        print(x,"is found")
    i+=1


#  print the element of the following list using a loop (for loop)
len=[1,4,9,16,25,36,49,81,100]
for nums in len:
    print(nums)

# search for a number X in this tuple (for loop)
tup=(1,4,9,16,25,36,49,81,100)    # we called it linear search in programing searching every no. 
x=25
i=0
for num in tup:
    if(num==x):
        print(i,"found")
    i+=1

# print number from 1 to 100
for i in range(1,101):
    print(i)
    

# print from 100 to 1
for i in range(100,0,-1):
    print(i)


# print the multiplication of number n
n=8
for i in range(1,11):
    print(n,"*",i,"=", n*i)


# WAP to find sum of n number (while using)
n=5
sum=0
for i in range(1,n+1):
    sum+=i
print("total sum is equal to:", sum)


# WAP to find a factorial of first n numbers
n=7
fact=1
for i in range (1,n+1):
    fact*=i
# print(fact)
