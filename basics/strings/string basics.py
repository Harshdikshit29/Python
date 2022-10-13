my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

my_string = """Hello, welcome to the
world of python"""
print(my_string)

#indexing
print(my_string[0])
print(my_string[-3])
print(my_string[2])
print(my_string[1])

#slicing
name = 'Thalapathi Vijay'
for i,c in enumerate(name):
    print(i,c)
print(name[-5: ])
print(name[ :11])
print(name[6:10])

#reverse the string
print(name[ : :-1])
print(name[:5][::-1])

#every even index char
print(name[::2])

#every odd index char
print(name[1::2])

#convert integer to string char
x = chr(65)
print(x)

# x = chr(2365)
# print(x)

# for i in range(15000,20000):
#     print(i,chr(i))

#convert char to integer
y = ord('A')
print(y)

y = ord('a')
print(y)

y = ord('{')
print(y)

y = ord('👀')
print(y)

# Concatenation (joining two or more string)
a = 'apple'
b = 'juice'
ab = a + b
print(ab)

w1 = 'this'
w2 = 'is'
w3 = 'Amazing'
msg = w1 + w2 + w3
print(msg)

#adding space between strings
msg = w1 + ' ' + w2 + ' ' + w3
print(msg)

#duplication
word = 'hi '
print(word * 3)

print('-' * 25)