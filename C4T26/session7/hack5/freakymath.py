import random
pts = 0
while True:
    a = random.randint(-20,20)
    b = random.randint(-20,20)
    c = random.randint(1,2)
    e = random.randint(1,2)
    if c == 1:
        d= a+b
        ope = '+'
    else:
        d = a-b
        ope = '-'
    if e == 1:
        x = random.randint(1,2)
        if x == 1:
            f = random.randint(-5,-1)
            d += f
        else:
            f = random.randint(1,5)
            d += f
    print(str(a) +' ' + ope+ ' '+ str(b)+' = '+str(d) )
    ans = input('yes or no: ')
    if ans == 'yes':
        if e == 2:
            print('correct')
            pts = pts+1
            print('points: '+str(pts))
        else:
            print('wrong')
            print('points: '+str(pts))
            break
    else:
        if e == 1:
            print('correct')
            pts = pts+1
            print('points: '+str(pts))
        else:
            print('wrong')
            print('points: '+str(pts))
            break