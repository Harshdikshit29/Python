# dictionary with integer keys
# my_dict = {1: 'apple', 2: 'ball'}
# print(my_dict)

val = ['Rajendra Singh', 30, 10, 'Accounts', 'Staff Officer', 600000, 7,]

val_dict = {
    'employee': 'Rajendra Singh', 'age': 30,
    'experience': 10, 'dept': 'Accounts',
    'designation': 'System Officer', 'salary': 600000,
    'team_size': 7
}

# displaying a dict
print(val_dict)

# retreival of value
ans = val_dict['designation'] # key in sqr brackets
print(ans)
print(val_dict['salary']) # correct
# print(val_dict['Experience']) # incorrect (key error)
print(val_dict['experience'])

# adding a data inside dict
val_dict['company'] = 'Acme.inc'
print(val_dict)
