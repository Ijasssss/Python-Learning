# Files I/O

f= open("sample.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()

""" Modes in files """
'''
r: open file for reading (DEFAULT)
w: open file file for writing , it erase evrything and overwrite from begning 
x: create a new file and open for writing 
a: open for writing, append to the end of the file
b: binary mode
t: text mode (DEFAULT)
+: open a file for updating or fot both (reading & writing)

'''

""" r: read """

f= open("sample.txt","r")

data=f.read(5) # reads the begning 5 characters
print(data)

line1=f.readline()
print(line1)
## there is gonna  be line in between becuase there is /n(new line added in in-built python)
line2=f.readline()
print(line2)

f.close()

""" w: write & a: append """

f= open("sample.txt","w")

f.write("My name is Ijas P ")
f.close()

f= open("sample.txt","a")

f.write("\n I am a Python Developer ")
f.close()



l= open("sample1.txt","a")
l.close()


""" r+ : (Reading & Writing)"""

f= open("sample.txt","r+")
f.write("hey")
print(f.read())
f.close()

""" w+ : (Writing & Reading )"""

f= open("sample.txt","w+")
print(f.read())
f.write("ijas")
f.close()


""" a+ : (append & writing)"""

f= open("sample.txt","a+")
print(f.read())
f.write(" P")
f.close()

""" [with] Syntax or (beter way for file) """ 

with open("sample.txt","r") as f:
    print(f.read())
    f.close() # if you does'nt close also the "with" syntax automatically close the file

""" Deleting a file """

import os # module (already created function or class ) to delete a file , no direct method 

os.remove("sample1.txt")# NOTE you have you have to use [os.remove("")]

""" Practise Questions """

''' Create a new file named practise.txt using python ad add the follwing data to it '''

with open("practise.txt","w") as f:
    f.write("Hi Everyone\now are learning file I/O\nUsing java\nI like programming in java")

''' WAF to  replace the occurance of java with pyhton in the above file '''

def replce():
    with open("practise.txt","r") as f:
        data= f.read()

    new_data =data.replace("java","Python")
    print(new_data)

    with open("practise.txt","w") as f:
        f.write(new_data)
replce()

''' Search the word "learning" exist in the file or not ?''' 

def check_word():
    with open("practise.txt","r") as f:
        data= f.read()
        new_data=data.find("learning")
        if(new_data==-1):
            print("DOesnot Exist")
        else:
            print("exist at",new_data,"Index")

check_word()

'''WAF to find the while line of the file does the word "learning" occur first
print -1 if the word doesnot found '''
def check_line():
    data= True
    word="Python"
    line = 1
    with open("practise.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print("found at line",line)
                return
            line+=1
    return print(-1)
check_line()

'''From a file containing numbers seperated by comma ,Print the count of Even numbers'''

with open("practise.txt","r") as f:
    data=f.read()
    print(data)
     
    split=data.split(",")
    print(split)
    
    
    count=0
    for val in split:
        if(int(val)%2==0):
            count=count+1
    print("The count of even numbers is ",count)
    
'''
This is an additional method to do seperate the numbers from the , in above question
    num=""
    for i in range(len(data)):
        if(data[i]==","):
            print(int(num))
            num=""
            
        else:
            num=num+data[i]
'''
