#Declaring a function  
a = 10
def add(): # function
    global a  #define global variable
    # Defining local variables. They has scope only within a function  
    # 4 space have 1 indiantation
    a = int(input('Enter First Number: '))  
    b = int(input("Enter Second Number: "))
    c = a + b  
    print("The sum is:", c)  

def sub(): # function
    global a  
    # Defining local variables. They has scope only within a function  
    # 4 space have 1 indiantation
    a = int(input('Enter First Number: '))  
    b = int(input("Enter Second Number: "))
    c = a - b  
    print("The sub is:", c)  
 
# Calling a function  
#add()
#sub()
del a #del keyword is used to delete a variable
#print(a)
'''
a = 10000000000000000000000000000000000000000000  
a = a -20000 
print(type(a))  
print (a)  
'''
a=20
print(a)
print((a))
a=20 
b=40
print(a,b) #Multiple Values Print


