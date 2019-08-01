while True:
    pw = input('password: ')
    a = pw.isalpha()
    if a == True:
        print('retry')
    else:
        if len(pw) <9:
            print('retry')
        else:
            print('good')
            break