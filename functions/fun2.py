def get_salary():
    val = int(input("Enter SALARY =>"))
    fine = .9
    return val * fine

print("salary", get_salary())

a = get_salary()
print('salary', a)

final_salary = get_salary() + 1000
print('salary', final_salary)


def amount():
    p = int(input('Principle:'))
    r = float(input('Rate:'))
    t = int(input('Time:'))
    si =  p * r * t / 100
    amt = si + p
    return amt, si

amt, si = amount()
print(f'the Amount will be {amt} on Simple interest {si}')
# or this way
print(f'the Amount will be {amount()[0]}')
    