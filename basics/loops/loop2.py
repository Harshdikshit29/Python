for i in range(100):
    print('Hello', i)

for i in range(100):
    print(i, end = '//')
    
for i in range(1,25):
    print(i ,end = ' ')

for i in range(1,15,2):
    print(i, end =' ')

for i in range(10, 0, -1): # Reverse Loop
    print(i, end = ' ')

print("=>")
data = [2,5,4,9,7,8]
for i in enumerate(data):
    print(i)


print("=>")
data = [2,5,4,9,7,8]
for i,d in enumerate(data):
    print(i, d)
    

print("=>")
data = [2,5,4,9,7,8]
for i,d in enumerate(data):
    print(i+1, d)

names = ['Apple','Banana','Cherry']
price = [100, 40, 65]

for n,p in zip(names, price):
    print(f'{n}=> Rs.{p}')