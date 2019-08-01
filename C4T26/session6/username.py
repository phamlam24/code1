while True:
    name = input('name: ')
    a = name.isalpha()
    if a == True:
        print('good')
        break
    else:
        print('retry')