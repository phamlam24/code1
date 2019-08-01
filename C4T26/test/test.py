map = []
for i in range(5):
    map.append([])
    for j in range(5):
        map[i].append('-')
def pmap(x):
    for i in range(x):
        for j in range(x):
            print(map[i][j], end=' ')
        print()
def movement(x):
    if move == 'w':
        if y1 != 0:
            map[x1][y1] = '-'
            y1 -=1
            map[x1][y1] = 'H'
    elif move == 'a':
        if x1 != 0:
            map[x1][y1] = '-'
            x1 -=1
            map[x1][y1] = 'H'
    elif move == 's':
        if y1 != 4:
            map[x1][y1] = '-'
            y1 +=1
            map[x1][y1] = 'H'
    elif move == 'd':
        if x1 != 4:
            map[x1][y1] = '-'
            x1 +=1
            map[x1][y1] = 'H'
    
availmoves =['w','a','s','d','wa','aw','wd','dw','sd','ds','as','sa']
y1 = x2 = 0
x1 = y2 = 4
map[0][4] = '1'
map[4][0] = '2'
pmap(5)
hp1 = 3
hp2 = 3
while True:
    while True:
        move1 = input('your move? ')
        if availmoves.count(move1) == 1:
            break
        else:
            print('invalid input')
    while True:
        shoot1 = input('your move? ')
        if availmoves.count(shoot1)  == 1:
            break
        else:
            print('invalid input')
    while True:
        move2 = input('your move? ')
        if availmoves.count(move2)  == 1:
            break
        else:
            print('invalid input')
    while True:
        shoot2 = input('your move? ')
        if availmoves.count(shoot2)  == 1:
            break
        else:
            print('invalid input')
    if 