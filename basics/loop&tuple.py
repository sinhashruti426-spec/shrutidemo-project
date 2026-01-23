 # WAP to ask user to name of their 3 favourite movies and store them in a list 
movie1=input("enter your first movie name: ")
movie2=input("enter your second movie name: ")
movie3=input("enter your third movie name: ")
fav_movie=[movie1,movie2,movie3]
print(fav_movie)

# WAP to check if a list contain palindrome of element (copy())
list=[3,2,1,2,3]
copy_list=list.copy()
list.reverse()
if(copy_list==list):
    print("palindrome")
else:
    print("not palindrome")
