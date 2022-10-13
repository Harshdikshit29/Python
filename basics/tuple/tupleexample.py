a = 1,2,3,4 # type => tuple
print(a)
print(type(a))

x,*y = 1,2,3,4,5,6 # to put 1 value in x and rest in y
print(x , y)
print(type(x), type(y)) 

x,y, *z = 1,2,3,4,5,6 # to put 1 value in x and 2nd in y and rest in z
print(x , y, z)
print(type(x), type(y), type(z))

x = (23,45,21,45) 
y = tuple([3,2,1,5]) # Concerting list to tuple

print(x,y)
print(type(x), type(y))