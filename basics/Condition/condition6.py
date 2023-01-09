email = input("Enter ur email=> ")

if '@' not in email:
    print('your email does not have @')
elif len(email) < 11:
    print('length of email not valid')
elif '.com' not in email and '.org' not in email:
    print('invalid domain')
else:
    print("your email look valid")
        