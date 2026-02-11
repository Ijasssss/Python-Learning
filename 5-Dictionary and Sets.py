# Dictionary 

''' key : value  ------> inamgine it as aword and meaning '''

info={
    "name":"ijas",
    "age":22,
    "height":169.99,
    "marks":[98.97,99],
    "is_adult":True,
    ("ijas"):(60,61,59,"ijas",78.99),
} 
info["name"]= "ijas P" # To change a value in key
info["name"]= "IJAS P" # it simply overwrite it doesnot create a ducplicate key value pair
info["college"]="Ramaiah University" # To add a key value pair to the dictionary
print(info["name"]) # to access or print a key in dictionary 
print(info["ijas"])
print(info["height"])
print(info["marks"])
print(info)

''' They are unordered , Mutable (Changable) , key duplication or (same key names ) are not alloweded '''

""" Empty Dictionary """

empty_dic={}

empty_dic["name"]="ijas"
empty_dic["age"]=22
print(empty_dic)


""" Nested Dictionary """

dic1={
    "name":"Ijas P",
    "marks":{
        "physics":99,        
        "maths":99,
        "chemistry":89
    },
    "age":22,
    "height":169.99,

}
print(dic1["marks"]["maths"]) # This is how you print a nested Dictionary

""" Dictionary Methods """

dic2={
    "fullname":"Mohammed ijas P",
    "name":{
        "first":"Mohamed",
        "Last": "Ijas P"
        },
    "age":23,
} 

print(dic2.keys()) ## Basically it prints all the "Keys" inside a the given  dictionary 
print(tuple(dic2.keys())) # Type Casted from (tuple list) dict ---> normal  tuple
print(len(dic2.keys())) # just printing the length  

print((dic2.values())) # It prints all the values i mean all including all the nested dictionaries
print(list(dic2.values())) # it convert the (tuple list )dictionary to  normal list 


print(dic2.items()) # it prints all the  {key:value} as tuples() 
print(list(dic2.items())) # The outer layer is converted to list 
a= list(dic2.items())
print((a[0])) # here i typecasted this dictionary method to list and perform the indexing which is not possible in dictionary because where it doesnot have an order


print(dic2.get("fullname")) # To get a value of a key in Method way
print(dic2["fullname"])# normal accessing or printing method 


dic2.update({"city":"Banglore","arts":"dancing"}) # you updated or added a key:value to the dictionary
dic3={"sports":"football"} # you create a new dictionary 
print(dic2.update(dic3)) # adding dictionay to existing dictionary instead of key:value
print(dic2)


# Sets
  
''' collection uniuqe elements , mutable ( CHANGABLE) "Elements are immutable " , No order (No indexing)'''

set1={"hello",1,1,1,1,1,1,1,2,"hello"} # doesnot repeat  more one time a datatype if it same 
print(set1)
print(len(set1)) # length is 3 so it take a datatype only once 

set2= set() # This is how you create an empty set 
set3={None} # This is alse how you can create an empty set just add None in curlybraces either its gonna show the type as dictionary
print(type(set2))
print(type(set3))


set4={1,2,3,(1,2,3)} # SETS ARE MUTABLE BUT ELEMENTS ARE IMMUTABLE , THEREFORE TUPLE IS ALLOWDED AND (LIST & DICTIONARY ) ARE NOT ALLOWDED

""" Set Methods """

set5=set()

set5.add("ijas") # to add an element to a set 
set5.add(1)
set5.add(1)
print(set5)


set5.remove(1) # To remove an elemnt from the set
print(set5)


set6={1,2,3,4,5,5}
set6.clear() # it clears out  everything in the set 
print(len(set6))
print((set6))


set7={4,2,3,6,7}
set7.pop() # It delete a random element from the set 
print(set7)
print(set7.pop()) # Shows the element deleted 


set8={1,2,3,4}
set9={4,5,6,7}
print(set8.union(set9)) # it Combined two sets using UNION
print(set8,set9) # No changes to default sets 

set8={1,2,3,4}
set9={4,5,6,7}
print(set8.intersection(set9)) # Prints the common Element in the set


""" Practise Questions """

''' store followimg word meanings in Python dictionary '''

meaning={
    "Table":["a piece of furniture","list of facts and figures"],
    "cat":"A Small Animal"
}
print(meaning)


'''list of subjects for students , one classroom is required for one subject.how many classroom are required by all subjects'''

subjects={"python","java","c++","python","javascript","java","python","java","c++","c"}
print("The Classroom required for the subjects:",len(subjects))


'''WAP to enter the marks of 3 subjects from user and store them in dictionary ,start with an empty dictionary and add one by one use 
subject name as key and mark as value ? '''

dictionary={}
sub1=float(input("Enter the marks of Maths:"))
dictionary.update({"Maths":sub1})
sub1=float(input("Enter the marks of Chemistry:"))
dictionary.update({"Chemistry":sub1})
sub1=float(input("Enter the marks of Physics:"))
dictionary.update({"Physics":sub1})
print(dictionary)


'''Figure out a way to store the 9 and  9.0 as a seperate values in set '''
 

set1={(9.0,9)} # Tuple
set2={9.0,"9",9} # floating value gets more priority than integer 
set3={("float,9.0"),("integer,9")} # string in the form of two tuples 
print(set1)
print(set2)
print(set3)