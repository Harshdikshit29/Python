#1 Create a string and print it.
x = "Hello"
print(x)

#2 Take a string input and print it's length.
new_string = input("Enter the string value: ")
print(len(new_string))

#3 Print the last word of the string "Python is great" using slices.
new_string = "Python is Great"
print(new_string[-1:])

#4 Print the each word in different line of string "python is everywhere".
new_string = "Python is everywhere"
for i in enumerate(new_string):
    print(i)

#5 Print the string Hello World! in reverse.
str = "Hello World!"
print(str[::-1])

#6 Convert the string How are you? in uppercase.
str = "How are you?"
print(str.upper())

#7 Convert the string How Is It Going? in lowercase.
str = "How Is It Going?"
print(str.lower())

#8 Join the following list by spaces( ) and print the result.
words = ['Python', 'is', 'easy', 'to', 'learn']
str = ' '.join(words)
print(str)

#9 Print a multiline string using a single print
# a)
str = """Hello
world
!"""
print(str)

# multiline string input
data = ''
while True:
    line = input()
    if not line:
        break
    data += line + '\n'
print(data)

#10 Print this string to move to newline '\n' is used. (results should look exactly like the provided string)
str = "Python"
print(f'Welcome \nto the {str}')

#11 Print a variable with some text using a single print function, output should look like following. (the variable is 15)
var = 15
print("the variable is",var)

#12 concatenate the following strings and print the result
s1 = 'python '
s2 = 'is '
s3 = 'great.'
str = s1 + s2 + s3
print(str)

#13 Print # 20 times without using a loop
str = '#'
print(str*20)

#14 Print numbers from 1 to 9, each on a seperate line, followed by a dot, output should look like the following-
# 1.
# 2.
# 3.

for i in range(1,10):
    print(f'{i}.')

#15 Ask user to input a sentence and print each word on a different line.
ent = input("enter a sentence: ")
for i,c in enumerate(ent):
    print(c)

#16 Ask user to input a string and check if the string ends with '?'
str = input("enter the string: ")
print(str.endswith("?"))

#17 Ask user to input a string and print how many times e appeared in the string
str = input("enter the string: ")
print('e occured -> ',str.count('e'))

#18 Check if the user input is a number.
x = input("enter: ")
print(x.isnumeric())

#19 Remove the extra spaces in beginning and in the end of the following string-
text = '   this is not a good string '
print(text.strip())

#20 Ask user to input string, print found if any of the character is upper case.
n = input('Enter the string: ')
print("The original string is : " + str(n))
res = False
for chr in n:
	if chr.isupper():
		res = True
		break
print("Does String contain uppercase : " + str(res))

#21 Extract names from the following string and store them in a list.
names = 'Joe, David, Mark, Tom, Chris, Robert'
li = list(names.split(" "))
print(li)

#22 In the following string, add aye in the end of every word and print the results.


#23 ask user to enter a string and check if the string contains fyi
n = input("enter a string: ")
if "fyi" in n:
    print("Yes fyi is present")
else:
    print("No, fyi is not present")

#24 Remove all the special characters and numbers from the following string
text = '%p34@y!-!t68h#&on404'
n = filter(str.isalpha,text)
x = "".join(n)
print(x)

#25 calculate the average word length of the following paragraph.
p = 'this is a paragraph which is written just for the purpose of providing content to let the average word length be calculated'
words = p.split()
avg = sum(len(word) for word in words) / (len(words))
print(avg)
