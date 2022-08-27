print(range(15))  
  
print(list(range(15)))  
  
print(list(range(4, 9)))  
  
print(list(range(5, 25, 4)))
#begain
num = int(input("Enter Any Number : "))
last = num*10 #last upto 10th place
listnum = list(range(num,last+1,num))#0,1,2,3,4,5,6,7,8,9
# 2+2+2+2 = 8 
simplenumber=list(range(1,101))
#print(simplenumber)
for j in listnum:
    print(j)
#end