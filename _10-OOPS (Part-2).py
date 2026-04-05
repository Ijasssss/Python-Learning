""" del Keyword """

''' del keyword are used to delete the object properties or object itself '''

class Student1:
    def __init__(self,name):
        self.name=name

s1 = Student1("ijas")
print(s1.name)
del s1.name
print(s1.name)

""" Private(like) attributes and methods """

''' conceptual implementation in python.
private attributes and methods are only accesible from  inside a class not from outside the class
'''

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no # this is public attribute
        self.__acc_pass=acc_pass # this is PRIVATE attribute [to make it PRIVATE just put 2 underscore "__" before the attribute]
    
    def reset_pass(self):
        print(self.__acc_pass)


cus1 = Account("123456","abcde")
print(cus1.acc_no) # can be accesed outside the class (PUBLIC)
# print(cus1.__acc_pass) # CANNOT be accesed outside the class (PRIVATE)

cus1.reset_pass() # calling the PRIVATE from the class through method



class Person1:
    __name="Anonymous" # Private attributes can only be accessed inside the class

    def __hello(self):
        print("Hello !")

    def welcome(self): # Private methods can only be accessed inside the class 
        self.__hello()

p1 = Person1()


print(p1.welcome()) # this is the use of Private method (if you are wondering what is the use of Private method)

""" IMPORTANT [OOPS] """

'''
3) INHERITANCE :
                When one class (Child/derived) derives the properties and methods of another class
                (Parent/Base)
'''

# (a) Single Inheritance

class Car2: # Parent (Base)

    oil="car oil is : shell"
    
    @staticmethod
    def start():
        print("Car Started!")
    @staticmethod
    def stop():
        print("Car Stopped!")

class ToyotaCar2(Car2): # Child (Inherited)

    def __init__(self,name):
        self.name=name

car1=ToyotaCar2("Fortuner")

print(car1.name)
car1.start() # Child object  able to use the method of Parent 
print(car1.oil) # Child object using the properties of the Parent 


# (b) Multi-Level Inheritance

class Car1: # GrandParent (Base)
    
    @staticmethod
    def start():
        print("Car Started!")
    @staticmethod
    def stop():
        print("Car Stopped!")

class ToyotaCar1(Car1): # Parent (Inherited)

    def __init__(self,brand):
        self.brand=brand


class Fortuner(ToyotaCar1):
    def __init__(self,type):
        self.type=type

car1 = Fortuner("Diesel")
car1.start() # Child Inherited from the GrandParent

# (c) Multiple Inheritance

class Physics:
    physics="Welcome to Physics !"

class Maths:
    maths="Welcome to Maths!"

class Student2(Physics,Maths):
    def __init__(self,name):
        self.name=name

s1 = Student2("ijas")

print(s1.physics) # Child Inherited from the parent 1
print(s1.maths) # Child Inherited from the parent 2

""" super() Method """

''' Used to call the methods( Constructor:properties) of parent class'''

class Car: 

    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("Car Started!")
    @staticmethod
    def stop():
        print("Car Stopped!")

class ToyotaCar(Car):

    def __init__(self,name,type):
        super().__init__(type) # calling constructor (attributes) of parent calss using super().__init(..)
        super().stop() # used to call methods of parent using super() 
        super().start() # no need to print this , the moment you create object on this class it gets print in FIFO
        self.name=name

c1= ToyotaCar("Land Cruiser","Diesel")

print(c1.type)


""" Class method (@Decorator) """

class Person:

    name="Anonymous"

    @classmethod
    def change_name(cls,name):
        cls.name=name

p1 = Person()
print(p1.name) 
p1.change_name("MOHAMMED IJAS P")
print(p1.name) # the above attribute "anonymous" present in the class is changed using (@classmethod) decorator method which is the method for class basically 


""" Property (@decorator) """

class Student:

    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    @property
    def cal_percentage(self):
        return (self.phy + self.chem + self.math)/3

stu1 = Student(99,98,99)

print(stu1.cal_percentage)

stu1.phy=92

print(stu1.cal_percentage)

""" IMPORTANT [OOPS] """

'''
4) POLYMORPHISM :
                 When a same operator is allowed to have diffferent meaning according to the 
                 context
'''

''' Operator Overloading :

                          it is the best example for Polymorphism

                          print(1 + 2) #3
                          print("hi "+ "how are you") # hi how are you
                          print([1,2] + [3,4]) # [1,2,3,4]

    
    Dunder function :
                       a + b -->  Addition       --> a.__add__(b)
                       a - b -->  Subtraction    --> a.__sub__(b)
                       a * b -->  multiplication --> a.__mul____(b)
                       a / b -->  division       --> a.__truediv____(b)
                       a % b -->  reminder       --> a.__mod____(b)
'''

class Complex:

    def __init__(self,real,img):
        self.real=real
        self.img=img

    def show(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2): # made another logic for "+" oprator using " Dunder Functions "
        newReal= self.real + num2.real
        newImg= self.img + num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self,num2): # made another logic for "-" oprator using " Dunder Functions "
        newReal= self.real - num2.real
        newImg= self.img - num2.img
        return Complex(newReal,newImg)

num1 = Complex(2,3)


num2= Complex(2,3)

num3 = num1 - num2 
num3.show()


""" Practise Questions """

''' Define a circle class to create circle with radius rusing the constructor
    define area method of the class which calculates the are aof the circle ,
    deine perimeter method of the class which allows you to calculate the perimeter of the cirlce
      '''
 

class Circle:

    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print("Th area is :",(22/7)*((self.radius)**2))
        
    def perimeter(self):
        print("The perimeter is :",(2 * (22/7)*self.radius))
        
c1 = Circle(21)
c1.area()
c1.perimeter()


''' Define a Employee class with attributes role, department & salary , this class also have a showdetails 
    method.
    create a another class engineer who inherits the properties of the employee and has additional
    attributes name and age 
    '''

class Employee:
    
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showdetails(self):
        print("role is :",self.role)
        print("department is :",self.department)
        print("salary is :",self.salary)


class Engineer(Employee):

    def __init__(self,name,age):
        self.name=name
        self.age=age 
        super().__init__("Engineer","IT","25 LPA")

        
e1= Engineer("Ijas","22")

e1.showdetails()


''' craete a class order which store items and its price 
    use dunder function __gt__() to convey that :
    order1>order2 if price of order1  > price of order2'''


class Order:

    def __init__(self,item,price):
        self.item=item
        self.price=price 

    def __gt__(self,o2 ):
        return self.price > o2.price


o1 = Order("lays",10)
o2 = Order("maggi",20) 
print(o2 > o1)