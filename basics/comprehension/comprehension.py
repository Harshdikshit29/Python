x = [1,2,3,4,5,6,7,8,9,10]

xsqr = [i**2 for i in x]
print(xsqr)

xodd = [i for i in x if i % 2 != 0]
print(xodd)

xevencube = [i**3 for i in x if i % 2 == 0]
print(xevencube)