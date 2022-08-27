numbers = []
len = int(input("Enter length of List : "))
for i in range(0,len): #0,1,2,3,4,5,6,7,8,9
    num = int(input("Enter Number : "))
    numbers.append(num)
cubevalue = 0 # value is 0

cube = []
print("The list of cube before loop is", cube)
for value in numbers:  
   
    #2*2*2  
    cubevalue = value*value*value #cube num*num*num
    cube.append(cubevalue)
    print("Cube of ",value," is ",cubevalue) 
    
print("The list of cube is", cube)
  