a = []
for i in range(10):
    n = int(input('enter the value: '))
    a.append(n)
print('the values entered were: ', a)

#Sum
print('sum of all the values entered are: ', int(sum(a)))

#Mean
print('mean of all the values entered are: ', sum(a)/len(a))

#Median

a.sort()
l = len(a)
m1 = a[l//2]
m2 = a[l//2 -1]
median = (m1 + m2)/ 2
print('median of the list is: ', median)

#Mode

