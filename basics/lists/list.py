
movies = ['DDLJ', 'fast & furious', 'Harry Potter', 'Iron Man', 'Shiddat', 'Sanam Teri Kasam',
              'Kuch kuch hota hai', 'Om Shanti Om', 'Jab we met', 'Shershah']

print(len(movies))

movies.sort()
print(movies)

movies.reverse()
print(movies)

print('first movie', movies[0])
print('last movie', movies[-1])
print('first 3 movies', movies[:3])
print('all movies except first 3', movies[3:])
print('movies with even indexes', movies[::2])

# #Example 2
books = ['The girl who knew too much', 'rich daddy', 'power of superconsious brain', 'beloved',
          'the key of success', 'harry potter']
books.append('3 mistakes of my life')
books.append('atomic habit')
books.append('you can win')
books.append('the final empire')

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}') 

books[8] = 'The well of Ascension'
books[-1] = 'Half Girlfriend'
books[2] = 'Legion'

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

books.insert(3, '2 States')
books.insert(5, 'Elantris')

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}') 

books.remove('atomic habit')
books.remove('Legion')

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}') 

#Extend Function

fruits = ['appple', 'banana', 'cherry', 'guava']
dry_fruits = ['almond', 'cashew', 'walnut']
fruits.extend(dry_fruits)
print(fruits)
print(dry_fruits)

#list sorting doesn't work in mixed datatype list

#remove is used to remove only 1 value at a time

x = [0,1,2,1,3,4,1,2,3,1,1,0,2,1,3,4,4,2,1,4,3,4]

x_zero = x.count(0)
x_one = x.count(1)
x_two = x.count(2)
x_three = x.count(3)
x_four = x.count(4)
print('0 occured', x_zero, 'times')
print('1 occured', x_one, 'times')
print('2 occured', x_two, 'times')
print('3 occured', x_three, 'times')
print('4 occured', x_four, 'times')

y = [22,23,24,25]
z = [12,2,3,4]

print('x adding y')
x.extend(y)
print(x)
print('x is adding z')
x.extend(z)
print(x)

xyz = x+y+z
print(xyz)

a = ['apple', 'banana', 'cherry', 'dragonfruit', 'elaichi']
v = a.pop(3) #pop removes value from an index
print(a)

lv = a.pop() #pop removes default value by default
print(a)
print(lv)