# Functions

''' Block of statement that does a Specific Task '''
'''If you want to do a Repeated(REDUNDANT) same task again and again , create and call a function'''

def sum_calc(a,b):# defining a function by function Name and as many parameters in the paranthesis
    sum=a+b
    return sum 
    
print(sum_calc(1,2))# calling a function by name and arguments( supply value )


def print_hello(): # if there is no parameter you can leave it as well 
    print("hello")

print_hello() # calling function 
print(print_hello()) # Because if you print a value which doesn't have a "return" value , it gets print None

''' Avearage of three numbers '''

def avg(a,b,c):
    sum=a+b+c
    count=3
    print(sum/count)
    return sum/count  # return can be reused , but print just shows
avg(1,2,3)


''' Default parameters in python '''

def mult(a=2,b=1):
    cross=a*b
    print(cross)
    return 
mult() # this works if no arguments are given , defult parameters are already fixed in function 

def fact(a,b=1):
    cross=a*b
    print(cross)
    return 
fact(1) # you can also set one default and for the other one arguments must be given ,and the giving arguments should be always start from the first one

"""Practise Questions"""

''' WAF to print the length of a list'''

cars=["bmw","toyota","suzuzki","audi","volkswagen"]
it_company=["Google","microsoft","apple","samsung","lenovo","Oneplus"]
def len_list(list):
    print(len(list))
    
len_list(cars)
len_list(it_company) 

'''WAF to print the elements in the list in a single line'''

cars=["bmw","toyota","suzuzki","audi","volkswagen","mahindra","porshe"]

def el_list(list):
    for i in list:
        print(i,end=" ")

el_list(cars)

'''WAF to find the factorial of n'''

def fact_n(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)

fact_n(5)

'''WAF to convert from  usd to inr'''

def usd_inr(usd):
    inr=usd*90.56
    print(usd,"USD=",inr,"INR")
    
usd_inr(1)

''' WAF where it find out odd or even '''

def odd_even(value):
    if (value%2==0):
        print(value,"is Even")
    else:
        print(value,"is Odd")

odd_even(int(input("Enter the digit")))


# Recursion 

def show(n):# imagine n=5 -->  n=4 -->  so on [Recursive function ]
    if (n==0):
        return
    print(n)
    show(n-1)
    print("End")


show(3)


def factorial(n):
    if (n==0 or n==1):
        return 1
    return  factorial(n-1)*n

print(factorial(3))

"""Practise Questions """

'''WA recursive function to calculate  sum of first n natural numbers '''

def sum_n(n):
    if(n==0):
        return 0

    return sum_n(n-1) + n

print(sum_n(2))


'''Write a recursive function to print all elements in a list'''

list1=[1,2,3,4,5,6,7,8]
list2=[1,2,3,4,5,6,7,8]  

def ele_list(list,index=0):
    if (index==len(list)):
        return
    print(list[index]) 
    return ele_list(list,index+1)

ele_list(list1)
     



