while True:
    price = int(input('enter price of item: '))
    if price < 0:
        break
    print(f'you entered {price} amout')
    
x = [1,2,3,4,-3,5,6,7,8,7,9]
for i in x:
    if i < 0:
        break
    print(i)