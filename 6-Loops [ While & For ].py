# Loops 

''' Are used for repeated instructions '''

""" While Loop """

i=1
while i<=5 :
    print("Hello")
    i += 1


i=1
while i<=10000 :
    print("MS Dhoni",i)
    i += 1
print(i)

''' print numbers from 1 to 5 & 5 to 1'''

i=5
while i>=1:
    print(i)
    i-=1

print("Loop Ended ")


''' print numbers from 1  to 100 '''

i=1
while i<=100 :
    print(i)
    i += 1

''' Print 100 to 1 '''

i=100
while i>=1:
    print(i)
    i-=1


''' print Multiplication table of number n '''

n=int(input("Enter Which table need to be printed ? : "))
i=1
while i<=10:
    print(n*i) # (n*1,n*2,n*3,n*4,.............)
    i=i+1

''' print the elements of the following list using loop '''

i=[1,4,9,16,25,36,49,64,81,100]
index=0
while  index < len(i):
    print(i[index])# i[0],i[1],i[2].....
    index = index+1 


''' search for a number x in this tulple using loop '''

x=int(input("Enter the digit to search :"))
tup=(1,2,3,4,37,45,24)
index=0

while index < len(tup):
    if(x==tup[index]):
        print("the given value",x,"is there")
    index=index+1 



""" Break & Continue """



i=1
while i <= 5:
    print(i)
    if(i==3):
        break
    i += 1

print("End of the Loop")



x=int(input("Enter the digit to search :"))
tup=(1,2,3,4,37,45,24)
index=0

while index < len(tup):
    if(x==tup[index]):
        print("the given value",x,"is there")
        break
    else:
        print("Finding")
    index=index+1 

print("End of the Loop")



i=1
while i <= 5:
    if(i==3):
        i+=1
        continue # Skip
    print(i)
    i += 1

print("End of the Loop")


'''print the numbers from 1 to 10  print only the odd number and skip the even number '''

i=0
while i<=10:
    if(i%2==0):
        i=i+1
        continue
    else:
        print(i)
    i=i+1


""" For Loop """

''' Bsically For loop traverse in a sequential way (Go through all indexs one by one ) 
like :- list ,tuple , strings '''

list1=[1,2,3] # For loop on lists

for val in list1: 
    print(val)



vegetables="potato" # For Loop on Strings

for val in vegetables:
    print(val)


tup1=(1,2,3,4,5) # for Loops on tuple

for val in tup1:
    print(val)


''' for and else '''

list2=[1,2,3,4,5]

for val in list2:
    if (val==3):
        print("3 found")
        break
    print(val)
else: # works after all the completion of [For]
    print("The value 3 Not Found")



'''Questions'''

''' print the elements of the following list using loops 
[1,,9,2,3,56,78,44,85,99]
'''

list3 = [1,9,2,3,56,78,44,85,99]

for val in list3:
    print(val)


''' Search for a value x in the tuple using Loop '''

tup2=(1,2,3,4,5,6)
x=int(input("Enter the value to Search:"))
index=0

for val in tup2:
    if(val==x):
        print("Value Found at index",index)
        break
    index=index+1     
else:
    print("Value not found")




""" range  """

''' It returns a sequence of numbers , where it start from 0 [Default], gets increment by 1 [Default] , stops before a given number'''
    
    
seq=range(5) # To know how the range works 
print(seq[0]) # 0
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4]) # 4

''' range ( start?, stop[Compulsory], step?[step size] )'''

for value in range(5):# range(stop) 
    print(value)

for value in range(2,10):# range(start,stop) 
    print(value)

''' printing from 1 to 100 all the even and odd numbers using range and loop '''

for value in range(2,101,2):# even 
    print(value)

for value in range(1,101,2):# odd 
    print(value)


'''Questions '''

''' Print number from 1 to 100 '''

for i in range(1,101):
    print(i)


''' print numbers from 100 to 1 '''

for i in range(100,0,-1):
    print(i)

'''Print the Multiplication table of a number n '''

n=int(input(" Enter the number for the table:"))

for value in range(1,11):
    print(n,"*",value,"=",n*value)
     


""" Pass """


for i in range(1,5):
    pass # It does nothing but can pass this for loop without any error (YOu can use it for Future Purpose )
print("hello")


if (1>=5):
    pass # can be used in if else or (conditional statements) statement
elif(1>=5):
    pass
else:
    pass

print("how are you!")


""" practise Questions """

''' Find a program to a find a sum of first n natural numbers (Using for & while loops )'''

n=int(input("Enter the digit:"))
sum=1
for i in range(1,n+1):
    sum = sum+i
print("Total:",sum)
    
n=int(input("Enter the digit "))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print("The total = ",sum)


'''WAP  to find the factorial of n numbers '''

fact=1
n=int(input("enter the Value: "))
for i in range(1,n+1):
    fact=fact*i
print("the factrial is :",fact)

n=int(input("Enter the digit :"))
i=1
fact=1
while i<=n:
    fact= fact*i
    i=i+1
print(fact)

