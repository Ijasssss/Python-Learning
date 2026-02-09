# Lists
marks = [99.9 , 78.5 , 39.99 , 67.89 , 78.66] # Square brakets and seperated by comma 

print(marks) 
print(type(marks)) # to print the Type of lists
print(len(marks)) # to print the Length of the lists
print(marks[0],marks[1]) # to print the  index of a List

random = ["ijas",22,"kerala ", 10.57] # in python you can store different types of data types in lists
print(random) 

'''
str="ijas"
str[0]="I"
print(str) 
print(str)

Strings are immutable in python (Cannot be changed by indexing )

'''

info = ["ijas",24,"kerala"]
info[0]="Ijas"
info[1]=22
info[2]="Malappuram , kerala "
print(info) # Lists are mutable ( which can change by indexing )

''' List Slicing '''

age=[22, 33, 45, 6, 66, 8]
print(age[:len(age)])
print(age[0:])
print(age[:len(age)])
print(age[-6:-2]) #  negative indexing 

""" List Methods """

'''if you try to print list methods inside a print function it gets updated and  prints as a "None" 
because in list it doesnot gets print updated results it has printed in strings
'''

list=[2, 1, 3,]
list1=["grapes","apple","banana"]
list.append(0) # adding an element to the end of the list
list.append(4)
print(list)

list.sort() # Sorting is done in ascending order for numbers
list1.sort() # sorting done in ascending order for alphabets too
print(list)
print(list1)

list.sort(reverse=True) # sorting done in descending order for numbers 
list1.sort(reverse=True) # sorting done in descending airder for alphabets too
print(list)
print(list1)

list2=["ijas",22, "banglore",170]
#list2.reverse() # basically it prints list in a reverse order
print(list2)

list2.insert(2,"B.tech") # inserting an element at a particular giving index --> (index,element)
print(list2)

list3=[3,1,2,1]
list3.remove(1) # it removes the element given by the user for the very first time seen on the list 
print(list3)

list4=[1,2,3,3,4,5] 
list4.pop(2)
print(list4)


# Tuple
'''
Tuple you CANNOT (Change , Add , Delete) once created 
'''
tup=("ijas",21,170,"banglore") # parenthesis and seperated by comma 
print(len(tup))
print(type(tup))

print(tup[0]) # indexing
print(tup[:len(tup)]) # slicing 

tup1=(1,)# if there is only one value in tuple you hava to add the value  and give a comma either if there is no comma python gonna think it as a integer 
print(type(tup1)) 
 
'''Tuple Methods'''

tup2=(1,2,3,4,1)
print(tup2.index(1)) # it prints the index of the given element

print(tup2.count(1)) # it prints the number of times the element present in tuple


""" Practice Questions """

''' WAP to user to enter the name of thier favourite movies and store them in list  '''

b=[]
a=input("enter your 3 favourite movies ?")
b.insert(0,a)
print(b)

'''or'''

c=[]
d=input("Enter the first fav movie?")
e=input("Enter the Second fav movie?")
f=input("Enter the Third fav movie?")
c.insert(0,d)
c.insert(1,e)
c.append(f)
print(c)

'''or '''

movies=[]
mov=input("Enter the First movie:")
movies.append(mov)
mov=input("Enter the Second movie:")
movies.append(mov)
mov=input("Enter the Third movie:")
movies.append(mov)
print(movies)

'''or'''

Movies=[]
Movies.append(input("Enter the First fav Movie:"))
Movies.append(input("Enter the Secoond fav Movie:"))
Movies.append(input("Enter the Third fav Movie:"))
print(Movies)

''' WAP check the list contains palindrome elements ?'''

list1=["IJAS",1,"IJAS"]
dup=list1.copy()
dup.reverse()


if (list1 == dup ):
    print("It is a palindrome")
else:
    print("NOT a palindrome")

'''WAP to count the numbers of students with "A" Grade in Tuple'''

Grades=("A","B","C","D","D","A","A","C","B","D")
print(Grades.count("A"))

''' store the above tuple values in a list and print them in "A" to "D" '''

grades=["A","B","C","D","D","A","A","C","B","D"]
grades.sort()
print(grades)
