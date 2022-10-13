from helper import read

data = read('pride_n_prejudice.txt')

print(len(data))

newData = data[3:50]
print(newData)

'''
formatting function
-lower
-upper
-swapcase
-capitalize
-title
casefold

-ljust
rjust
-center
'''
print(newData.lower())
print(newData.upper())
print(newData.swapcase())
print(newData.capitalize())
print(newData.title())
print(newData.casefold())

word = 'hello'
spacing = 20
ljust = word.ljust(spacing,'😘')
print(ljust)
rjust = word.rjust(spacing,'👀')
print(rjust)
cen = word.center(spacing,'🌹')
print(cen)

#vailidation function - either true or false
print(newData.isupper())
print(newData.islower())
print(newData.isalpha())
print(newData.isnumeric())
print