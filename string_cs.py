# string basic operator
"""
1. find
2. replace
3. capitalize
4. endswith
"""
str="i am a coder"
print(str.find("am")) #2 output showed
print(str.replace("a","o")) #it will replace a with o 
print(str.capitalize())  #capitalize first word of character
print(str.endswith("er"))  #it will show True or False if the given character ends with the word 


# conditional statements
num=int(input("enter a number: "))
if(num%2==0):
  print("even")
else:
  print("odd")

# grade by conditional statement
marks=int(input("enter a number: ")) 
if(marks>=90):
  print("Grade:A")
elif(90>marks>=80):
  print("Grade:B")
elif(80>marks>=70):
  print("Grade:C")
elif(70>marks>=30):
  print("Grade:D")
else:
  print("fail")


# Nested statement
digit=float(input("enter a digit: "))
if(digit>=0):
    if(digit==0):
        print("zero digit")
    elif(digit>0):
        print("positive digit")
else:
    print("negative digit")
