#1 WAP to create a list of 5 names taken from user and then display each name in reverse

#2 WAP to print a fibonacci series using the concept of list (0,1,1,2,3,5,8,11....)

#3 WAP to generate a new list that contains sqaures of each numbers from existing list e.x x= [2.3,4,5] => [4,8,16,25]

#4 WAP to generate a new list from an existing list of numbers that contains only odd numbers

#5 WAP to generate a new list by adding 2 list element wise


#1
names = []
for i in range(5):
    names.append(input("names=> "))
for name in names:
    print(name[::-1])
 
#2
fib = [0,1]
for i in range(15):
    fib.append(fib[-1] + fib[-2])
print(fib)   

#3
x = [1,2,3,4,5,6,7,8,9]
x2 = []
for num in x:
    x2.append(num ** 2)
print(x)
print(x2)

#4
a = [1,2,3,4,5,6,7,8,9,10,11]
aodd = []
for i in a:
    if i % 2 != 0:
        aodd.append(i)
print(aodd)

#5
a=[1,2,3,4,5]
b=[6,7,8,9,10]
c= []
for i,j in zip(a,b):
    c.append(i+j)
print(a)
print(b)
print(c)
