#Strings 

'''Escape Sequence Character '''

str1 = "My name is ijas.\nand I am From India " # Generally \n gives us New Line in between sentences 
str2 = "I am 21 years Old\t i do coding a bit " # Generally \t gives us tab space in between sentences
print(str1)
print(str2)

''' Concatenation '''

str3="ijas"
str4="p"
concatenated_string= (str3+str4)
print(concatenated_string)
print(str3+str4)

''' Lenght of the String '''

str5= "I am a Good Student"
len1=len(str5)
print(len(str5)) # Python includes the spaces also as the length not only the words or Letter
print(len1)


print(concatenated_string + " " + str5)
print(len(concatenated_string + " " + str5))

''' Indexing'''

str6="ijas p"
print(str6[0]) # Indexing starts From zero and spaces and special characyters is is also included 

''' Slicing'''

str7="MS Dhoni" # total only 7 index 
print(str7[0:8])# this means 0:7 , till 8 it doesnot gets printed
print(str7[:7]) # it means it starts from zero = 0:6
print(str7[0:]) # this means it ends in the last = 0:(or Last)   or to the lenght of string 
print(str7[0:len(str7)]) # from 0 --> till the end of the string  or length of the string

''' Negative Slicing'''

str8="Apna"
print(str8[-4:-1])
print(str8[-4:])


''' String Functions '''

str="i am learning  python"
print(str.endswith("on")) # Check wheather the the sring ends with this given character if yes it prints True else False

print(str.capitalize()) # capitalize the first letter of the sentences , only the first words first letter
print(str) # it only will work for the capitalized form , else all will be the default string which means no capitalization will occur 
str=str.capitalize()
print(str) # therefore  it works now only it is completely modified

print(str.replace("a","o")) # basically replaces the old with new (old,new) 
print(str.replace("python","Java script"))
 
print(str.find("l")) # Here it prints the index of the the "letter" it exist in the string and for the first time occurance only 
print(str.find("Q")) # if we print something its not there it gives us -1

print(str.count("a")) # it prints the number of times the letter or word occur in the string 


""" Practise Questions """

''' input user name and print its length''' 

name=input("Enter Your First Name :")
print("the length of the string name is :",len(name))

''' find the occurance of '$' in string'''

num="i have 5$ in my hand i give 4$ to my friend and am left with 1$ wiht me "
print(num.count("$"))

# Conditional Statements 

age=21
if(age>=18):
    print("The Person can Vote and apply for licence")
elif(age<18):
    print("Cannot Vote")

light="green "
if(light=="red"): # starts from here 
    print("stop")
elif(light=="green"): # checks elif statements if the "if" statement is false
    print("go")
elif(light=="yellow"): # checks if the upper elif is false
    print("Wait")
else:
    print("Erroe with lights") 
print("Traffic Signal Over") # works if all the above is false 


num=10
if (num>2):
    print("the number is greater than 2 ") # the if statement always get checked everytime or how manytimes you write 
if (num>3):
    print("The number is greater than 3") # it also goes through this if statement

''' when something is true it gets kicked  out of the conditional statement completely ''' 

'''marks based conditional statements '''

marks=float(input("Enter the student marks:"))
if (marks>=90):
    grade ="A"
elif(90>marks and  marks>=80):
    grade="B"
elif (80>marks and marks>=70):
    grade="C"
else:
    grade="D"
print("Grade of the student is :",grade)


''' Nesting '''

age= int(input("Enter the age ?"))
if (age>=18):
    if(age>=50):
        print("age over")
    else:
        print("can vote")
else:
    print("CANNOT Vote")
 

""" Practice Questions """

''' WAP to check the number entered by the user is odd or even '''

num=int(input("Enter The Number:"))
if((num%2)==0):
    print("The Number",num,"Even Number")
elif((num%2)!=0):
    print("The Number is Odd")

''' WAP Find the greatest of three Numbers'''

a=int(input("Enter the First Number:"))
b=int(input("Enter the Second Number:"))
c=int(input("Enter the Third Number:"))
if(a>=b and a>=c):
    print("The First Number given",a,"is the greatest number ")
elif ( b>=c):
    print("The Second Number given",b,"is the greatest number ")
else:
    print("The Third  Number given",c,"is the greatest number ")

''' WAP to find the largest among 4 numbers'''

a=int(input("Enter the first number:"))
b=int(input("Enter the Second number:"))
c=int(input("Enter the Third number:"))
d=int(input("Enter the Fourth number:"))
if ((a>=b and a>=c )and a>=d):
    print(a,"The first Number is greatest")
elif(b>=c and b>=d):
    print(b,"The Second Number is greatest")
elif(c>=d):
    print(c,"The Third Number is greatest")
else:
    print(d,"The Fourth Number is greatest")

''' WAP Check the given number is multiple of 7 ? '''

num=int(input("Enter the digit:"))
if((num%7) == 0):
    print(num,"It's a multiple of 7")
elif((num%7) != 0):
    print(num,"Not a multiple of 7")


