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
print(newData.isalnum())

# Split
words = newData.split()
print(words)

names = "Amar, Akbar, Anthony, Vijay, Deenanath" # str
name_list = names.split(",") # list

for nm in name_list:
    print('name->',nm)

items = input("enter 5 items seperated by space: ").split()
print(items)

# join
data_list = ['Python','-m','textblob']

result = " ".join(data_list)
print(result)
result = ", ".join(data_list)
print(result)
result = "".join(data_list)
print(result)
result = "_O_".join(data_list)
print(result)

# replace
msg = newData.replace("not","yes")
print(msg)