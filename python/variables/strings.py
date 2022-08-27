str = "Hello Helpdrive "
str1 = "Welcome Here"

print(str[0:9])
print(str[4])
print(str*2)
print(str+str1)

#working on python list
list1  = [1, "hi", "Python", 2,"Helpdrive"]
list2 = [1,"ram","rohan",5,45.7]
list3 = list1+list2
print(list1[1])
print(type(list1))
print (list1[1:])
print (list1[0:2])
print(list1+list2)

#working on python tuples
tuple = ("mohan","raj",10)
tuple2 = ("jay","rahul")
print(tuple)
print(type(tuple))
print (tuple[1:])  #slicing  
print (tuple[0:1]) #slicing
print (tuple+tuple2)  #concatenation using + operator  
print(tuple * 2) # Tuple repatation using * operator  
list2[2] = "hi"
print(list2)