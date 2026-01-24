 # dictionaries
dict={"name":"shruti sinha","course":"CSE","rollno.":25033301000141}
print(type(dict))
dict["name"]="parv chaudray" # it assign new value by replacing older one
print(dict)
dict["sem"]="second" # we can also add an key and value in dict
print(dict)
print(dict["name"])    # by this we can see value of particular key
print(dict.keys())
print(dict.values())
print(dict.get("course"))
print(dict.items())    # it show keys and values in tuple
dict.update({"year":"first"}) # to add new dictionary
print(dict)




# sets
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
set1.add(10)
set1.remove(3)
set1.pop()    #randomly delete any element
print(set1.union(set2))
print(set1.intersection(set2))
