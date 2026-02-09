# Variables in Python 

name ="ijas" #string 
age=22 # integer
price=32.99 #float
print(name,age)
''' There for here the name  and age are callerd "variables"
and they are used to store data values ,so the values are ijas and 22 respectively 
'''
#ASSIGNING ANOTHER VARIBALE TO A EXIXTING VARIABLE 

name2 =name 
print(name2) 
''' Here what happened is when you store a value of a variable to another variable it copies the vaule of first vaiable to second variable
'''
# Finiding out the type of the varibale 

name ="ijas" #string 
age=22 # integer
price=32.99 #float

print(type(name))
print(type(age))
print(type(price)) 



#OPERATORS 

string_name1='ijas'
string_name2="ijas" 
string_name3='''ijas''' # you can use single quotes , double quotes , triple quotes to store a string 
integer_age=22 #integer can +ve , _ve values and zero(0)

#Float 
price = 36.99 # float is the value with decimal points

#Boolean

age_above_18 = True # careful "T" should be capitalized
age_below_18 = False # careful "F" should be capitalized

print(type(age_above_18))

#NONE

age=None
print(type(age))


#keywords

'''  keywords are resrved words in python that cannot be used as the varibles
therefore the keywords are :-  [ True,None,False,if,else,elif,break,continue,while,is,in,def,and  ]    etc.....'''

#print sum 

a=10
b=20
sum=a+b
print(a+b,sum) # you can do it two ways to print a sum 


#operators

''' Aithmatic operators
# [+,-,/,*,%,**] 
'''
a=20
b=2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)# This is called "Modulus" :- T his usually gives the reminder when you divide two numbers 
print(a**b)# a^b :- like a to the power of b

'''Relational or Comparison Operators
 [==,!=,>,>=,<,<=]
 '''
a=20
b=30

print(a==b)# checking :- the answer will be False
print(a!=b)#True
print(a>b)#False
print(a>=b)#False
print(a<b)#True
print(a<=b)#True

# Assignment Opretors
''' [=,+=,-=,*=,/=,%=,**=]
'''
num=10
num+=5 # num=num+5
num-=5 # num=num-5
num*=5 # num=num*5
num/=5 # num=num/5
num%=5 # num=num%5
num**=5 # num=num**5
print(num)


 # Logical Operators 

'''[NOT , AND , OR]'''

val1=10
val2=20
print('NOT Operator:', not (val1>val2)) # not
print('NOT Operator:', not True) # not

val3=True
val4=False

print("AND Oprator:",(val3 and val4)) # AND
print("OR Oprator:",(val3 or val4)) # OR
print("OR Oprator:",(val1==val2) or (val1<=val2)) # OR , Here i used Comparison oprator and Logical operator 

#Type Casting 

a=float("4")
b=5 
print(type(a))
print(a+b) # Manual Type Casting 

# input

B= input("Enter yor Name:") #this will be inbuilt "string" if you want to change you need to forcefully change 
print("Welcome",B)

A = int(input("Enter you age :")) # Basically "input" is we are asking the user to give the value and accept the user's value
print("Your age is:", A)

C = float(input("Enter the Overall Price :")) # Basically "input" is we are asking the user to give the value and accept the user's value
print("Overall price is:", C)

''' EXAMPLE'''
 
name1=input("Enter your name :")
print("Your name is:",name1)
age1=int((input("Enter your Age :")))
print("Your age is:",age1)
marks=float((input("Enter your Marks:")))
print("Your Marks is:",marks)

# Practise Questions 

'''input 2 numbers and print their sum'''
a=int((input('Enter the First number:')))
b=int((input('Enter the Second  number:')))
print("The answer for the the sum is :",(a+b))

'''write a program to input the side of a square and  print its area '''

side= float(input("Enter the sides of the Square :"))
print("The Area of the square is a^2 =",(side**2))

'''program to give an input of two floating numbers and find its  avearage  '''

a=float(input("Enter the First Number:"))
b=float(input("Enter the Second Number:"))
sum=a+b
count=2
print("The Avearage of two Numbers are",(sum/count))

''' program to input two integer number a and b , print true if a is greater than or equal to b and if not print false '''
a=int(input("enter the first number :"))
b=int(input("enter the second number :"))
print(a>=b) 




