email = input("Enter ur email=> ")

if '@' in email:
    if len(email) >= 11:
        if '.com' in email or 'org' in email:
            print("your email look valid")
        else:
            print('invalid domain')
    else:
        print('length of email not valid')
else:
    print('your email does not have @')