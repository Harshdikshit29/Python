# tuple - set -list (interchangeable)

x = [1,2,3,4,5,6,7,8,9,6,6,7,9,2,2]
xt = tuple(x) # list - tuple
xl = list(xt) # tuple - list
xs = set(x) # list - set
xl = list(xs) # set - list
xs = set(xt) # tuple - set
xt = tuple(xs) # set - tuple

print(x)
print(xt)
print(xl)
print(xs)
print(xl)
print(xs)
print(xt)

# WAP to create a tuple, by taking ten inputs from the user

a= []
for i in range(10):
    n=input("enter the numbers: ")
    a.append(n)

print(tuple(a))
