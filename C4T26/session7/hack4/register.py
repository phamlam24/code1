a = input('ten dang nhap: ')
while True:
    b = input('mat khau: ')
    if len(b) <8:
        print('mat khau phai co 8 chu so')
    elif b.isalpha() ==True:
        print('mat khau phai co ca chu va so')
    else:
        break
while True:
    c = input('email: ')
    if ('@' in c == False):
        print('email phai co @')
    elif('.' in c == False):
        print('email phai co dau cham')
    else:
        break
print(a + ' ' + b + ' '+ c)