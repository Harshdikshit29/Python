# Arithmetic Operators
a=12
b=9
print('Arithmetic Operators')
print(a+b) #addition
print(a-b) #substraction
print(a*b) #multiplication
print(a/b) #division
print(a//b) #rounded off (quotient)
print(a%b) #remainder
print(a**b) #exponentiation (power)

# Assingment Operators
print('Assingment Operators') # (simple assingment)
x=15
y= x+15
z= x+y
a= x**2 + y**2
print(x,y,z,a)

print('Updation Operator') # (updation assingment)
b= 10
b+= 5
print(b)
b-= 2
print(b)
b*= 3
print(b)
b/= 2
print(b)

# Comparison Operator
a=100
b=40
print('Comparison Operator')
print(a==100)
print(b==100)
print(a== b+60)
print(5==3)
print(a!=b)
print(b!=20)
print(a<=500)
print(a>=500)

# Logical Operators
print('Logical Operators')
a=10
b=9
c=11
print(a>b and a>c)
print(a>b and a<c)
print(a>b or a>c)
print(a>b or a<c)
print(a<b or a>c)
print(a<b and a>c)
print(not a>b)
print(not False)
print(not True)

# in Operator
print('in operator')
names = ['Harsh', 'Niketa', 'Ekansh']
print('priya' in names)
print('Niketa' in names)
print('Ekansh' in names)
print('Harsh' in names)

message = 'Once upon a time, there was a person'
print('upon' in message)
print('there' in message)
print('that is' in message)

#is operator
print('IN OPERATOR')
x = 10
y = 10
z = x
c = 5
d = 10
print(x is y)
print(x is c)
print(x is z)
print(y is z)
print(y is x)
print(c is x)
print(c is c)
print(c is d)
print(x is d)

x = [1,2,3]
y = [1,2,3]
z = x
print(x is y)
print(x is z)
print(z is y)