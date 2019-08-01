thelist = ['a','b','c','d']
while True:
    a = input('choose your function: ')
    if a == 'C':
        create = input('add your item: ')
        thelist.append(create)
    elif a == 'R':
        read = int(input('position to see: '))
        print(thelist[read - 1])
    elif a == 'U':
        update = int(input('position: '))
        thelist[update - 1] = input('change? ')
    elif a == 'D':
        delete = int(input('position: '))
        thelist.pop(delete - 1)
    elif a == 'E':
        break
    else:
        print('invalid')
    print(thelist)
print(thelist)