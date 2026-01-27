# average of number
def avg (a,b,c):
    sum=a+b+c
    avg=sum/3
    return avg
print(avg(1,2,3))


# WAF to print the lenghth of a list. (list is the parameter)
l=[1,2,3,4,5,6,7,8,9]
def calc_len(l):
    return l
print(len(l))


# WAF to print the elements of the list in a single line
def calc_len(l):
    print(l)
    return l
calc_len(l)

#      or
def calc_len(l):
    for num in list:
        print(l, end=" ")
print(len(l))

# WAFto find a factorial n
def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
calc_fact(5)


# wite a function to convert USD to INR
def converter(usd_value):
    inr_value=usd_value*92
    print(usd_value,"usd","=",inr_value,"inr")
converter(2)


# even or odd
def num(n):
    n=int(input("enter a number:"))
    if n%2==0:
        print("even")
        return
    else:
        print("odd")
num(5)

# recursive function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(6)

# factorial by recursion
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
print(fact(3))


#  write a recursive function to calculate the first of n natural number
def sum(n):
    if(n==0):
        return 0
    else:
        return n + sum(n-1)
print(sum(9))


# write a recursive function to print all elements in list 
def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
city=["mumbai","chennai","pune","muzzafarpur","hyderabad"]
# print_list(city)
