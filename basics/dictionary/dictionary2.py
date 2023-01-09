from pprint import pp

movies = {}
movies['Top Gun: Maverick'] = 8.3
movies['EEAO'] = 8.1
movies['Spider Man: No way home'] = 8.2
print(movies)

for item in movies:
    print(item)

print('only values')
for item in movies:
    print(movies[item])
    
print('both key and values')
for key in movies:
    print(key, movies[key])

print('using dict.items() method')
for k,v in movies.items():
    print(k,v)

# user input
for i in range(3):
    name = input('movie name: ')
    rating = float(input(' movie rating: '))
    movies[name] = rating

print('using dict.items() method')
for k,v in movies.items():
    print(k,v)