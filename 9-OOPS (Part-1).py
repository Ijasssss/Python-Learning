# OOPS [Object Oriented Programming Sysytem]

'''To map with real World scenario we started using class & objects'''

class Students: # Creating a class
    name="karan"

s1=Students() # Created a object from the above class
print(s1.name)

s2=Students()
print(s1.name)

""" __init__ (constructor) """

''' A constructor is created and called automatically even if we dont create or 
when a object is call  or created under the class in python '''

class Student:

    ''' There is Going to be one default constructor before
    parameterized constructor '''

    def __init__(self,name, marks): # parametertized constructor 
        self.name=name
        self.marks=marks
        print("Student names are:")

s1 = Student("ijas",98) # constructor is being called 
print(s1.name,s1.marks) # printing this

s2 = Student("naji",99) # Constructor is being called again 
print(s2.name,s2.marks) # and printing this 


""" Class & object/instance attributes(data) """

class Student1:
    college_name="Abc College"
    name="Anonymous"

    def __init__(self,name,marks):
        self.name=name # object/instance attributes in name
        self.marks=marks

s1= Student1("ijas",99)
print(s1.name,s1.marks)
print(s1.college_name) # class attribute calling on object name  
print(Student1.college_name) # class attribute calling on class name

""" Methods """

''' Methods are the functions that belongs to objects '''

class Student2:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def welcome(self): # This is a method for objects
        print("Welcome Student:",self.name) # gets print the given objects name

    def getmarks(self): # one more method
        return self.marks


s1= Student2("ijas",99)
s1.welcome() # calling a method
print(s1.getmarks()) # Again calling a method 

""" Practise Question """

'''create  student class that takes name and marks of 3 subjects as argument in constructor 
the create a mthod to print the avearage'''

class Student3:
     
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def avg(self):
        sum=0
        for i in self.marks:
            sum=sum+i
        print("Hello",self.name,", Your avg score of 3 subjects are ",sum/3)
        

s1= Student3("ijas",[99,99,99])
s1.avg()

s1.name="MOAHMMED IJAS P"
s1.avg()


""" Static Methods """

'''methods that doesn't use the self parameter (works at class Level)'''

class Student4:

    def __init__(self,name): # Constructor
        self.name=name
    
    @staticmethod # Decorator (To change the normal behaviour of the function in Both Input & Output)
    def hello(): # Static Method
        print("Hello how are you")

    def morning(self): # Normal Method
        print("Hi",self.name,"Good Morning")


s1= Student4("ijas")
s1.morning()
s1.hello() # No Error Occur due to mentioning of staticmethod Decorator       
    


""" IMPORTANT [OOPS] """
'''
1) ABSTRACTION :
                Hiding the implementation details in class and showing only the essential 
                features to the user.

2) ENCAPSULATION:
                Wrapping the data(Attributes) and functions intoma single unit (Object)

'''

""" Practise Questions """

''' Create a class Account with 2 attributes account number & balance, 
    and create methods for credit,debit and printing balance
'''

class Account:

    def __init__(self,acc_no,balance):
        self.acc_no=acc_no
        self.balance=balance

    def debit(self,amount):
        self.balance = self.balance - amount
        print("The debitted Amount is :",amount)
        print("The Total Balance is :",self.get_balance())

    def credit(self,amount):
        self.balance = self.balance + amount
        print("The Credited Amount is :",amount)
        print("The Total Balance is :",self.get_balance())

    def get_balance(self):
        return self.balance
        
cus1= Account(12345678,1000)
cus1.debit(550)