import random
import math
swlvl = 0
shlvl = 0
arlvl = 0
bolvl = 0
yaaay = 0
map =[]
def pmap():
    for i in range(6):
        for j in range(6):
            print(map[i][j], end=' ')
        print()
def pmap1():
    for i in range(10):
        for j in range(10):
            print(map[i][j], end=' ')
        print()
                        # LEVEL 1
for i in range(6):
    map.append([])
    for j in range(6):
        map[i].append('-')
x1 = random.randint(0,5)
y1 = random.randint(0,5)
map[x1][y1] = 'H'
while True:     # create key pos
    x2 = random.randint(0,5)
    y2 = random.randint(0,5)
    if x1 != x2 or y1 != y2:    
        map[x2][y2] = 'K'
        break
while True:         #create door pos
    x3 = random.randint(0,5)
    y3 = random.randint(0,5)
    if (x1 != x3 or y1 != y3) and (x2 != x3 or y2 != y3):
        map[x3][y3] = 'D'
        break
while True:         # create wall
    x4 = random.randint(0,5)
    y4 = random.randint(0,5)
    if (x1 != x4 or y1 != y4) and (x2 != x4 or y2 != y4) and (x3 != x4 or y3 != y4):
        map[x4][y4] = 'W'
        break
pmap()
key = 0
prefx = x1
prefy = y1
print('LEVEL1')
while True:  # basic movement controls
    move = input('Your move? ')
    if move == 'w':
        if x1 != 0:
            map[x1][y1] = '-'
            x1 -=1
            map[x1][y1] = 'H'
    elif move == 'a':
        if y1 != 0:
            map[x1][y1] = '-'
            y1 -=1
            map[x1][y1] = 'H'
    elif move == 's':
        if x1 != 5:
            map[x1][y1] = '-'
            x1 +=1
            map[x1][y1] = 'H'
    elif move == 'd':
        if y1 != 5:
            map[x1][y1] = '-'
            y1 +=1
            map[x1][y1] = 'H'
    elif move == 'c':
        print('sneaky arent you?')
        break
    else:
        print('invalid')
    if x1 == x2 and y1 == y2:
        print('you just obtained a key')
        key += 1
    if x1 == x3 and y1 == y3:
        if key == 0:
            print('you need to obtain a key first')
        else:
            print('you finished lvl1')
            break
    if prefx == x3 and prefy == y3:
        map[x3][y3] = 'D'
    if x1 == x4 and y1 == y4:
        print('you cant walk though walls, this isnt a magic game')
        x1 = prefx
        y1 = prefy
        map[x1][y1] = 'H'
        map[x4][y4] = 'W'
    prefx = x1
    prefy = y1
    pmap()

#                                   LEVEL 2
map = []
for i in range(6):
    map.append([])
    for j in range(6):
        map[i].append('-')
x1 = random.randint(0,5)
y1 = random.randint(0,5)
map[x1][y1] = 'H'
while True:     # create key pos
    x2 = random.randint(0,5)
    y2 = random.randint(0,5)
    if x1 != x2 or y1 != y2:    
        map[x2][y2] = 'K'
        break
while True:         #create door pos
    x3 = random.randint(0,5)
    y3 = random.randint(0,5)
    if (x1 != x3 or y1 != y3) and (x2 != x3 or y2 != y3):
        map[x3][y3] = 'D'
        break
while True:         # create wall
    x4 = random.randint(0,5)
    y4 = random.randint(0,5)
    if (x1 != x4 or y1 != y4) and (x2 != x4 or y2 != y4) and (x3 != x4 or y3 != y4):
        map[x4][y4] = 'W'
        break
while True:         # create key2 (5)
    x5 = random.randint(0,5)
    y5 = random.randint(0,5)
    if (x1 != x5 or y1 != y5) and (x2 != x5 or y2 != y5) and (x3 != x5 or y3 != y5) and (x4 != x5 or y4 != y5):
        map[x5][y5] = 'K'
        break
while True:         # create wall 2 (6)
    x6 = random.randint(0,5)
    y6 = random.randint(0,5)
    if (x1 != x6 or y1 != y6) and (x2 != x6 or y2 != y6) and (x5 != x6 or y5 != y6) and (x3 != x6 or y3!= y6):
        map[x6][y6] = 'W'
        break
pmap()
key = 0
prefx = x1
prefy = y1
print('LEVEL 2')
while True:  # basic movement controls
    move = input('Your move? ')
    if move == 'w':
        if x1 != 0:
            map[x1][y1] = '-'
            x1 -=1
            map[x1][y1] = 'H'
    elif move == 'a':
        if y1 != 0:
            map[x1][y1] = '-'
            y1 -=1
            map[x1][y1] = 'H'
    elif move == 's':
        if x1 != 5:
            map[x1][y1] = '-'
            x1 +=1
            map[x1][y1] = 'H'
    elif move == 'd':
        if y1 != 5:
            map[x1][y1] = '-'
            y1 +=1
            map[x1][y1] = 'H'
    elif move == 'c':
        print('sneaky arent you?')
        break
    else:
        print('invalid')
    if (x1 == x2 and y1 == y2) or (x1 == x5 and y1 == y5):
        print('you just obtained a key')
        key += 1
    if x1 == x3 and y1 == y3:
        if key <2:
            print('you need to obtain a key first')
        else:
            print('you finished lvl2')
            break
    if prefx == x3 and prefy == y3:
        map[x3][y3] = 'D'
    if (x1 == x4 and y1 == y4) or (x1 == x6 and y1 == y6):
        print('you cant walk though walls, this isnt a magic game')
        x1 = prefx
        y1 = prefy
        map[x1][y1] = 'H'
        map[x4][y4] = 'W'
        map[x6][y6] = 'W'
    prefx = x1
    prefy = y1
    pmap()

# LEVEL 3

hero = {
    'HP' : 20,
    'damage': 10,
    'reload': 3,
    'stack': 3,
    'defense': 5,
    'curHP' : 20,
    'curdamage': 10,
    'curreload': 3,
    'curstack': 3,
    'curdefense': 5,
    'crirate': 10,
    'cridmg': 2,
    'defHP' : 20,
    'defdamage': 10,
    'defdefense': 5,
    'flee': 1
}
monster = {
    'baseHP': 10,
    'basedamage': 6,
    'basedefense': 5,
    'HP' : 10,
    'damage': 6,
    'defense': 5,
    'flee': 0.3,
    'curHP' : 10,
    'curdamage': 6,
    'curreload': 2,
    'curstack': 1,
    'curdefense': 5,
    'rate': 0.2,
    'crirate': 2,
    'cridmg': 2
}
monsmax = 3
monscount = 0
map = []
for i in range(6):
    map.append([])
    for j in range(6):
        map[i].append('-')
x1 = random.randint(0,5)
y1 = random.randint(0,5)
map[x1][y1] = 'H'
while True:     # create key pos
    x2 = random.randint(0,5)
    y2 = random.randint(0,5)
    if x1 != x2 or y1 != y2:    
        map[x2][y2] = 'K'
        break
while True:         #create door pos
    x3 = random.randint(0,5)
    y3 = random.randint(0,5)
    if (x1 != x3 or y1 != y3) and (x2 != x3 or y2 != y3):
        map[x3][y3] = 'D'
        break
while True:         # create wall
    x4 = random.randint(0,5)
    y4 = random.randint(0,5)
    if (x1 != x4 or y1 != y4) and (x2 != x4 or y2 != y4) and (x3 != x4 or y3 != y4):
        map[x4][y4] = 'W'
        break
while True:         # create key2 (5)
    x5 = random.randint(0,5)
    y5 = random.randint(0,5)
    if (x1 != x5 or y1 != y5) and (x2 != x5 or y2 != y5) and (x3 != x5 or y3 != y5) and (x4 != x5 or y4 != y5):
        map[x5][y5] = 'K'
        break
while True:         # create wall 2 (6)
    x6 = random.randint(0,5)
    y6 = random.randint(0,5)
    if (x1 != x6 or y1 != y6) and (x2 != x6 or y2 != y6) and (x5 != x6 or y5 != y6) and (x3 != x6 or y3!= y6):
        map[x6][y6] = 'W'
        break
pmap()
key = 0
prefx = x1
prefy = y1
print('LEVEL 3')
print('Beware of Monsters!')
while True:  # basic movement controls
    move = input('Your move? ')
    if move == 'w':
        if x1 != 0:
            map[x1][y1] = '-'
            x1 -=1
            map[x1][y1] = 'H'
    elif move == 'a':
        if y1 != 0:
            map[x1][y1] = '-'
            y1 -=1
            map[x1][y1] = 'H'
    elif move == 's':
        if x1 != 5:
            map[x1][y1] = '-'
            x1 +=1
            map[x1][y1] = 'H'
    elif move == 'd':
        if y1 != 5:
            map[x1][y1] = '-'
            y1 +=1
            map[x1][y1] = 'H'
    elif move == 'c':
        print('sneaky arent you?')
        break
    else:
        print('invalid')
    if (x1 == x2 and y1 == y2) or (x1 == x5 and y1 == y5):
        print('you just obtained a key')
        key += 1
    if x1 == x3 and y1 == y3:
        if key <2:
            print('you need to obtain a key first')
        else:
            print('you finished lvl3')
            break
    if prefx == x3 and prefy == y3:
        map[x3][y3] = 'D'
    if (x1 == x4 and y1 == y4) or (x1 == x6 and y1 == y6):
        print('you cant walk though walls, this isnt a magic game')
        x1 = prefx
        y1 = prefy
        map[x1][y1] = 'H'
        map[x4][y4] = 'W'
        map[x6][y6] = 'W'
    if monscount < monsmax:
        mons = random.random()
        if mons <= monster['rate']:
            print('Encountered a monster!')
            while monster['curHP'] >0 and hero['curHP'] >0:
                print('HP: '+str(hero['curHP'])+ '     Monster HP: '+str(monster['curHP'])),
                action = input('choose from atk(1), def(2) or run(3): ')
                if action == 'atk' or action == '1':
                    if hero['curstack'] > 0:
                        dmg = hero['curdamage'] - monster['curdefense']
                        if dmg<=0:
                            dmg = 1
                        monster['curHP'] = monster['curHP'] - dmg
                        print('Hero dealt '+ str(dmg)+' damage!')
                        hero['curstack'] -=1
                    else:
                        print('No energy left for attack!')
                elif action == 'def' or action =='2':
                    hero['curdefense'] = math.floor(hero['defense'] *1.5)
                    hero['curstack'] += 1
                elif action == 'run' or action == '3':
                    fleee = random.random()
                    if fleee >= (hero['flee'] - monster['flee']):
                        print('Got away safely!')
                        break
                    else:
                        print('Cant escape!')
                        hero['curstack'] += 1
                dmg = monster['curdamage'] - hero['curdefense']
                if dmg <=0:
                    dmg = 1
                hero['curHP'] = hero['curHP'] - dmg
                print('Monster dealt '+ str(dmg)+' damage!')
                hero['curdefense'] = hero['defense']
            if monster['curHP']<=0:
                print('Monster have been defeated!')
                monscount += 1
            elif hero['curHP'] <0:
                print('You have been defeated.')
                break
    monster['curHP'] = monster['HP']
    monster['curdamage'] = monster['damage']
    monster['curdefense'] = monster['defense']
    prefx = x1
    prefy = y1
    pmap()
    print('HP: ', str(hero['curHP']))

#                       LEVEL 4:
monster['baseHP'] +=1
monster['HP'] = monster['baseHP']
monster['HPbox'] = 0.1
monsmax = 4
monscount = 0
icount = 0
hpboxmax = 2
hpcount = 0

map = []
for i in range(6):
    map.append([])
    for j in range(6):
        map[i].append('-')
x1 = random.randint(0,5)
y1 = random.randint(0,5)
map[x1][y1] = 'H'
while True:     # create key pos
    x2 = random.randint(0,5)
    y2 = random.randint(0,5)
    if x1 != x2 or y1 != y2:    
        map[x2][y2] = 'K'
        break
while True:         #create door pos
    x3 = random.randint(0,5)
    y3 = random.randint(0,5)
    if (x1 != x3 or y1 != y3) and (x2 != x3 or y2 != y3):
        map[x3][y3] = 'D'
        break
while True:         # create wall
    x4 = random.randint(0,5)
    y4 = random.randint(0,5)
    if (x1 != x4 or y1 != y4) and (x2 != x4 or y2 != y4) and (x3 != x4 or y3 != y4):
        map[x4][y4] = 'W'
        break
while True:         # create key2 (5)
    x5 = random.randint(0,5)
    y5 = random.randint(0,5)
    if (x1 != x5 or y1 != y5) and (x2 != x5 or y2 != y5) and (x3 != x5 or y3 != y5) and (x4 != x5 or y4 != y5):
        map[x5][y5] = 'K'
        break
while True:         # create wall 2 (6)
    x6 = random.randint(0,5)
    y6 = random.randint(0,5)
    if (x1 != x6 or y1 != y6) and (x2 != x6 or y2 != y6) and (x5 != x6 or y5 != y6) and (x3 != x6 or y3!= y6):
        map[x6][y6] = 'W'
        break
while True:         # create wall 3 (7)
    x7 = random.randint(0,5)
    y7 = random.randint(0,5)
    if (x1 != x7 or y1 != y7) and (x2 != x7 or y2 != y7) and (x5 != x7 or y5 != y7) and (x3 != x6 or y3!= y6):
        map[x7][y7] = 'W'
        break
pmap()
key = 0
prefx = x1
prefy = y1
print('LEVEL 4')
print('There is a chance to get the HP box in every turn!')
while True:  # basic movement controls
    monster['curHP'] = monster['HP']
    monster['curdamage'] = monster['damage']
    monster['curdefense'] = monster['defense']
    move = input('Your move? ')
    if move == 'w':
        if x1 != 0:
            map[x1][y1] = '-'
            x1 -=1
            map[x1][y1] = 'H'
    elif move == 'a':
        if y1 != 0:
            map[x1][y1] = '-'
            y1 -=1
            map[x1][y1] = 'H'
    elif move == 's':
        if x1 != 5:
            map[x1][y1] = '-'
            x1 +=1
            map[x1][y1] = 'H'
    elif move == 'd':
        if y1 != 5:
            map[x1][y1] = '-'
            y1 +=1
            map[x1][y1] = 'H'
    elif move == 'c':
        print('sneaky arent you?')
        break
    else:
        print('invalid')
    if (x1 == x2 and y1 == y2) or (x1 == x5 and y1 == y5):
        print('you just obtained a key')
        key += 1
    if x1 == x3 and y1 == y3:
        if key <2:
            print('you need to obtain a key first')
        else:
            print('you finished lvl4')
            break
    if prefx == x3 and prefy == y3:
        map[x3][y3] = 'D'
    if (x1 == x4 and y1 == y4) or (x1 == x6 and y1 == y6) or (x1 == x7 and y1 == y7):
        print('you cant walk though walls, this isnt a magic game')
        x1 = prefx
        y1 = prefy
        map[x1][y1] = 'H'
        map[x4][y4] = 'W'
        map[x6][y6] = 'W'
        map[x7][y7] = 'W'
    if monscount < monsmax:
        mons = random.random()
        if mons <= monster['rate']:
            print('Encountered a monster!')
            while monster['curHP'] >0 and hero['curHP'] >0:
                print('HP: '+str(hero['curHP'])+ '     Monster HP: '+str(monster['curHP'])),
                action = input('choose from atk(1), def(2) or run(3): ')
                if action == 'atk' or action == '1':
                    if hero['curstack'] > 0:
                        dmg = hero['curdamage'] - monster['curdefense']
                        if dmg<=0:
                            dmg = 1
                        monster['curHP'] = monster['curHP'] - dmg
                        print('Hero dealt '+ str(dmg)+' damage!')
                        hero['curstack'] -=1
                    else:
                        print('No energy left for attack!')
                elif action == 'def' or action =='2':
                    hero['curdefense'] = math.floor(hero['defense'] *1.5)
                    hero['curstack'] += 1
                elif action == 'run' or action == '3':
                    fleee = random.random()
                    if fleee <= (hero['flee'] - monster['flee']):
                        print('Got away safely!')
                        break
                    else:
                        print('Cant escape!')
                        hero['curstack'] += 1
                dmg = monster['curdamage'] - hero['curdefense']
                if dmg <=0:
                    dmg = 1
                hero['curHP'] = hero['curHP'] - dmg
                print('Monster dealt '+ str(dmg)+' damage!')
                hero['curdefense'] = hero['defense']
            if monster['curHP']<=0:
                print('Monster have been defeated!')
                monscount += 1
            elif hero['curHP'] <0:
                print('You have been defeated.')
                break
    if hpcount <hpboxmax:
        hprand = random.random()
        if hprand <= monster['HPbox']:
            print('Got a HP box!')
            hero['curHP'] = hero['HP']
            hpcount += 1
    prefx = x1
    prefy = y1
    pmap()
    print('HP: ', str(hero['curHP']))

#           LEVEL 5:
level = 5
equip = {
    'armor': 0,
    'boots': 0,
    'sword': 0,
    'shield': 0
}
whatitem = random.randint(1,4)
monster['baseHP'] +=1
monster['HP'] = monster['baseHP']
monster['HPbox'] = 0.09
monster['flee'] += 0.03
monsmax = 4
monscount = 0
icount = 0
hpboxmax = 2
hpcount = 0

map = []
for i in range(6):
    map.append([])
    for j in range(6):
        map[i].append('-')
x0 = random.randint(0,5)
y0 = random.randint(0,5)
x1 = random.randint(0,5)  # create item pos
y1 = random.randint(0,5)
map[x1][y1] = 'H'
while True:     # create key pos
    x2 = random.randint(0,5)
    y2 = random.randint(0,5)
    if x1 != x2 or y1 != y2:    
        map[x2][y2] = 'K'
        break
while True:         #create door pos
    x3 = random.randint(0,5)
    y3 = random.randint(0,5)
    if (x1 != x3 or y1 != y3) and (x2 != x3 or y2 != y3):
        map[x3][y3] = 'D'
        break
while True:         # create wall
    x4 = random.randint(0,5)
    y4 = random.randint(0,5)
    if (x1 != x4 or y1 != y4) and (x2 != x4 or y2 != y4) and (x3 != x4 or y3 != y4):
        map[x4][y4] = 'W'
        break
while True:         # create key2 (5)
    x5 = random.randint(0,5)
    y5 = random.randint(0,5)
    if (x1 != x5 or y1 != y5) and (x2 != x5 or y2 != y5) and (x3 != x5 or y3 != y5) and (x4 != x5 or y4 != y5):
        map[x5][y5] = 'K'
        break
while True:         # create wall 2 (6)
    x6 = random.randint(0,5)
    y6 = random.randint(0,5)
    if (x1 != x6 or y1 != y6) and (x2 != x6 or y2 != y6) and (x5 != x6 or y5 != y6) and (x3 != x6 or y3!= y6):
        map[x6][y6] = 'W'
        break
while True:         # create wall 3 (7)
    x7 = random.randint(0,5)
    y7 = random.randint(0,5)
    if (x1 != x7 or y1 != y7) and (x2 != x7 or y2 != y7) and (x5 != x7 or y5 != y7)and(x3 != x6 or y3!= y6):
        map[x7][y7] = 'W'
        break
pmap()
key = 0
prefx = x1
prefy = y1
print('LEVEL 5')
print('There is a chance to get an item')
while True:  # basic movement controls
    monster['curHP'] = monster['HP']
    monster['curdamage'] = monster['damage']
    monster['curdefense'] = monster['defense']
    move = input('Your move? ')
    if move == 'w':
        if x1 != 0:
            map[x1][y1] = '-'
            x1 -=1
            map[x1][y1] = 'H'
    elif move == 'a':
        if y1 != 0:
            map[x1][y1] = '-'
            y1 -=1
            map[x1][y1] = 'H'
    elif move == 's':
        if x1 != 5:
            map[x1][y1] = '-'
            x1 +=1
            map[x1][y1] = 'H'
    elif move == 'd':
        if y1 != 5:
            map[x1][y1] = '-'
            y1 +=1
            map[x1][y1] = 'H'
    elif move == 'c':
        print('sneaky arent you?')
        break
    elif move == 'e':
        print('sword: '+str(equip['sword']))
        print('shield: '+str(equip['shield']))
        print('armor: '+str(equip['armor']))
        print('boots: '+str(equip['boots']))
    else:
        print('invalid')
    if (x1 == x2 and y1 == y2) or (x1 == x5 and y1 == y5):
        print('you just obtained a key')
        key += 1
    if x1 == x3 and y1 == y3:
        if key <2:
            print('you need to obtain a key first')
        else:
            print('you finished lvl ' + str(level))
            break
    if prefx == x3 and prefy == y3:
        map[x3][y3] = 'D'
    if (x1 == x4 and y1 == y4) or (x1 == x6 and y1 == y6) or (x1 == x7 and y1 == y7):
        print('you cant walk though walls, this isnt a magic game')
        x1 = prefx
        y1 = prefy
        map[x1][y1] = 'H'
        map[x4][y4] = 'W'
        map[x6][y6] = 'W'
        map[x7][y7] = 'W'
    if monscount < monsmax:
        mons = random.random()
        if mons <= monster['rate'] and move != 'e':
            print('Encountered a monster!')
            while monster['curHP'] >0 and hero['curHP'] >0:
                print('HP: '+str(hero['curHP'])+ '     Monster HP: '+str(monster['curHP'])),
                action = input('choose from atk(1), def(2) or run(3): ')
                if action == 'atk' or action == '1':
                    if hero['curstack'] > 0:
                        dmg = hero['curdamage'] - monster['curdefense']
                        if dmg<=0:
                            dmg = 1
                        monster['curHP'] = monster['curHP'] - dmg
                        print('Hero dealt '+ str(dmg)+' damage!')
                        hero['curstack'] -=1
                    else:
                        print('No energy left for attack!')
                elif action == 'def' or action =='2':
                    hero['curdefense'] = math.floor(hero['defense'] *1.5)
                    hero['curstack'] += 1
                elif action == 'run' or action == '3':
                    fleee = random.random()
                    if fleee <= monster['flee']:
                        print('Got away safely!')
                        break
                    else:
                        print('Cant escape!')
                        hero['curstack'] += 1
                dmg = monster['curdamage'] - hero['curdefense']
                if dmg <=0:
                    dmg = 1
                hero['curHP'] = hero['curHP'] - dmg
                print('Monster dealt '+ str(dmg)+' damage!')
                hero['curdefense'] = hero['defense']
            if monster['curHP']<=0:
                print('Monster have been defeated!')
                monscount += 1
            elif hero['curHP'] <0:
                print('You have been defeated.')
                break
    if hpcount <hpboxmax:
        hprand = random.random()
        if hprand <= monster['HPbox']:
            print('Got a HP box!')
            hero['curHP'] = hero['HP']
            hpcount += 1
    if x0 == x1 and y0 == y1:
        if whatitem ==1:
            if equip['sword'] == 0:
                hero['damage'] += 1
                hero['curdamage'] += 1
                print('Got a sword!')
                equip['sword'] +=1
            else:
                hero['damage'] += 1
                hero['curdamage'] += 1
                print('Sword upgraded!')
                equip['sword'] +=1
        elif whatitem ==2:
            if equip['shield'] == 0:
                hero['defense'] += 1
                hero['curdefense'] += 1
                print('Got a shield!')
                equip['shield'] +=1
            else:
                hero['defense'] += 1
                hero['curdefense'] += 1
                print('Shield upgraded!')
                equip['shield'] +=1
        elif whatitem ==3:
            if equip['armor'] == 0:
                hero['HP'] += 3
                hero['curHP'] += 1
                print('Got an armor!')
                equip['armor'] +=1
            else:
                hero['HP'] += 3
                hero['curHP'] += 3
                print('Armor upgraded!')
                equip['curHP'] +=1
        else:
            if equip['boots'] == 0:
                hero['flee'] += 0.1
                print('Got boots!')
                equip['sword'] +=1
            else:
                hero['flee'] += 0.1
                print('Boots upgraded!')
                equip['boots'] +=1
    prefx = x1
    prefy = y1
    pmap()
    print('HP: ', str(hero['curHP']))

#                       LEVEL 6:
level += 1
whatitem = random.randint(1,4)
monster['baseHP'] +=1
monster['HPbox'] = 0.09
monster['flee'] += 0.03
monsmax = 4
monscount = 0
icount = 0
hpboxmax = 2
hpcount = 0

map = []
for i in range(6):
    map.append([])
    for j in range(6):
        map[i].append('-')
x0 = random.randint(0,5)
y0 = random.randint(0,5)
x1 = random.randint(0,5)  # create item pos
y1 = random.randint(0,5)
map[x1][y1] = 'H'
while True:     # create key pos
    x2 = random.randint(0,5)
    y2 = random.randint(0,5)
    if x1 != x2 or y1 != y2:    
        map[x2][y2] = 'K'
        break
while True:         #create door pos
    x3 = random.randint(0,5)
    y3 = random.randint(0,5)
    if (x1 != x3 or y1 != y3) and (x2 != x3 or y2 != y3):
        map[x3][y3] = 'D'
        break
while True:         # create wall
    x4 = random.randint(0,5)
    y4 = random.randint(0,5)
    if (x1 != x4 or y1 != y4) and (x2 != x4 or y2 != y4) and (x3 != x4 or y3 != y4):
        map[x4][y4] = 'W'
        break
while True:         # create key2 (5)
    x5 = random.randint(0,5)
    y5 = random.randint(0,5)
    if (x1 != x5 or y1 != y5) and (x2 != x5 or y2 != y5) and (x3 != x5 or y3 != y5) and (x4 != x5 or y4 != y5):
        map[x5][y5] = 'K'
        break
while True:         # create wall 2 (6)
    x6 = random.randint(0,5)
    y6 = random.randint(0,5)
    if (x1 != x6 or y1 != y6) and (x2 != x6 or y2 != y6) and (x5 != x6 or y5 != y6) and (x3 != x6 or y3!= y6):
        map[x6][y6] = 'W'
        break
while True:         # create wall 3 (7)
    x7 = random.randint(0,5)
    y7 = random.randint(0,5)
    if (x1 != x7 or y1 != y7) and (x2 != x7 or y2 != y7) and (x5 != x7 or y5 != y7)and(x3 != x6 or y3!= y6):
        map[x7][y7] = 'W'
        break
pmap()
key = 0
prefx = x1
prefy = y1
print('LEVEL 6')
print('Randomized monster and critical damage!')
while True:  # basic movement controls
    monster['curHP'] = monster['HP']
    monster['curdamage'] = monster['damage']
    monster['curdefense'] = monster['defense']
    move = input('Your move? ')
    if move == 'w':
        if x1 != 0:
            map[x1][y1] = '-'
            x1 -=1
            map[x1][y1] = 'H'
    elif move == 'a':
        if y1 != 0:
            map[x1][y1] = '-'
            y1 -=1
            map[x1][y1] = 'H'
    elif move == 's':
        if x1 != 5:
            map[x1][y1] = '-'
            x1 +=1
            map[x1][y1] = 'H'
    elif move == 'd':
        if y1 != 5:
            map[x1][y1] = '-'
            y1 +=1
            map[x1][y1] = 'H'
    elif move == 'c':
        print('sneaky arent you?')
        break
    elif move == 'e':
        print('sword: '+str(equip['sword']))
        print('shield: '+str(equip['shield']))
        print('armor: '+str(equip['armor']))
        print('boots: '+str(equip['boots']))
    else:
        print('invalid')
    if (x1 == x2 and y1 == y2) or (x1 == x5 and y1 == y5):
        print('you just obtained a key')
        key += 1
    if x1 == x3 and y1 == y3:
        if key <2:
            print('you need to obtain a key first')
        else:
            print('you finished lvl ' + str(level))
            break
    if prefx == x3 and prefy == y3:
        map[x3][y3] = 'D'
    if (x1 == x4 and y1 == y4) or (x1 == x6 and y1 == y6) or (x1 == x7 and y1 == y7):
        print('you cant walk though walls, this isnt a magic game')
        x1 = prefx
        y1 = prefy
        map[x1][y1] = 'H'
        map[x4][y4] = 'W'
        map[x6][y6] = 'W'
        map[x7][y7] = 'W'
    if monscount < monsmax:
        mons = random.random()
        monster['HP'] = monster['baseHP'] + random.randint(-2,2)
        monster['damage'] = monster['basedamage'] + random.randint(-1,1)
        monster['defense'] = monster['basedefense'] + random.randint(-1,1)
        if mons <= monster['rate'] and move != 'e':
            print('Encountered a monster!')
            while monster['curHP'] >0 and hero['curHP'] >0:
                print('HP: '+str(hero['curHP'])+ '     Monster HP: '+str(monster['curHP'])),
                action = input('choose from atk(1), def(2) or run(3): ')
                if action == 'atk' or action == '1':
                    crit = random.randint(1,100)
                    critm = random.randint(1,100)
                    if hero['crirate'] >= crit:
                        hero['curdamage'] = hero['curdamage'] * hero['cridmg']
                    if monster['crirate'] >= critm:
                        monster['curdamage'] = monster['curdamage'] * monster['cridmg']
                    if hero['curstack'] > 0:
                        dmg = hero['curdamage'] - monster['curdefense']
                        if dmg<=0:
                            dmg = 1
                        monster['curHP'] = monster['curHP'] - dmg
                        print('Hero dealt '+ str(dmg)+' damage!')
                        hero['curstack'] -=1
                    else:
                        print('No energy left for attack!')
                    if hero['crirate'] >= crit:
                        hero['curdamage'] = hero['curdamage'] / hero['cridmg']
                    if monster['crirate'] >= critm:
                        monster['curdamage'] = monster['curdamage'] / monster['cridmg']
                elif action == 'def' or action =='2':
                    hero['curdefense'] = math.floor(hero['defense'] *1.5)
                    hero['curstack'] += 1
                elif action == 'run' or action == '3':
                    fleee = random.random()
                    if fleee <= monster['flee']:
                        print('Got away safely!')
                        break
                    else:
                        print('Cant escape!')
                        hero['curstack'] += 1
                dmg = monster['curdamage'] - hero['curdefense']
                if dmg <=0:
                    dmg = 1
                hero['curHP'] = hero['curHP'] - dmg
                print('Monster dealt '+ str(dmg)+' damage!')
                hero['curdefense'] = hero['defense']
            if monster['curHP']<=0:
                print('Monster have been defeated!')
                monscount += 1
            elif hero['curHP'] <0:
                print('You have been defeated.')
                break
    if hpcount <hpboxmax:
        hprand = random.random()
        if hprand <= monster['HPbox']:
            print('Got a HP box!')
            hero['curHP'] = hero['HP']
            hpcount += 1
    if x0 == x1 and y0 == y1:
        if whatitem ==1:
            if equip['sword'] == 0:
                hero['damage'] += 1
                hero['curdamage'] += 1
                print('Got a sword!')
                equip['sword'] +=1
            else:
                hero['damage'] += 1
                hero['curdamage'] += 1
                print('Sword upgraded!')
                equip['sword'] +=1
        elif whatitem ==2:
            if equip['shield'] == 0:
                hero['defense'] += 1
                hero['curdefense'] += 1
                print('Got a shield!')
                equip['shield'] +=1
            else:
                hero['defense'] += 1
                hero['curdefense'] += 1
                print('Shield upgraded!')
                equip['shield'] +=1
        elif whatitem ==3:
            if equip['armor'] == 0:
                hero['HP'] += 3
                hero['curHP'] += 1
                print('Got an armor!')
                equip['armor'] +=1
            else:
                hero['HP'] += 3
                hero['curHP'] += 3
                print('Armor upgraded!')
                equip['curHP'] +=1
        else:
            if equip['boots'] == 0:
                hero['flee'] += 0.1
                print('Got boots!')
                equip['sword'] +=1
            else:
                hero['flee'] += 0.1
                print('Boots upgraded!')
                equip['boots'] +=1
    prefx = x1
    prefy = y1
    pmap()
    print('HP: ', str(hero['curHP']))
#                       FREEPLAY:
# xatk = 0
# xdef = 0
# distr = 0
# herodefeat = 0
# wallbreak = 0
# while True:
#     equipco = 0

#     level += 1
#     monster['baseHP'] +=1
#     if level % 2 == 0:
#         monster['basedefense'] +=1
#     if level % 2 == 1:
#         monster['basedamage'] += 1
#     if level % 3 == 0:
#         monster['flee'] += 0.1
#         monsmax += 1
#     elif level % 3 == 2:
#         if monster['HPbox'] > 0.01:
#             monster['HPbox'] -= 0.01
#         monster['crirate'] += 2
#         monster['rate'] += 0.01
#     else:
#         monster['baseHP'] += 1
#         monster['cridmg'] += 0.2
#     monster['HPbox'] = 0.09
#     monster['flee'] += 0.03
#     monscount = 0
#     icount = 0
#     hpboxmax = 2
#     hpcount = 0
#     imax = 2
#     map = []
#     for i in range(10):
#         map.append([])
#         for j in range(10):
#             map[i].append('-')
#     x0 = random.randint(0,9)
#     y0 = random.randint(0,9)
#     x1 = random.randint(0,9)  # create item pos
#     y1 = random.randint(0,9)
#     xx1 = random.randint(0,9)
#     yy1 = random.randint(0,9)
#     xx2 = random.randint(0,9)
#     yy2 = random.randint(0,9)
#     xx3 = random.randint(0,9)
#     yy3 = random.randint(0,9)
#     xx4 = random.randint(0,9)
#     yy4 = random.randint(0,9)
#     xx5 = random.randint(0,9)
#     yy5 = random.randint(0,9)
#     map[x1][y1] = 'H'
#     while True:     # create key pos
#         x2 = random.randint(0,9)
#         y2 = random.randint(0,9)
#         if x1 != x2 or y1 != y2:    
#             map[x2][y2] = 'K'
#             break
#     while True:         #create door pos
#         x3 = random.randint(0,9)
#         y3 = random.randint(0,9)
#         if (x1 != x3 or y1 != y3) and (x2 != x3 or y2 != y3):
#             map[x3][y3] = 'D'
#             break
#     while True:         # create wall
#         x4 = random.randint(1,8)
#         y4 = random.randint(1,8)
#         if (x1 != x4 or y1 != y4) and (x2 != x4 or y2 != y4) and (x3 != x4 or y3 != y4):
#             map[x4][y4] = 'W'
#             break
#     while True:         # create key2 (5)
#         x5 = random.randint(0,9)
#         y5 = random.randint(0,9)
#         if (x1 != x5 or y1 != y5) and (x2 != x5 or y2 != y5) and (x3 != x5 or y3 != y5) and (x4 != x5 or y4 != y5):
#             map[x5][y5] = 'K'
#             break
#     while True:         # create wall 2 (6)
#         x6 = random.randint(1,8)
#         y6 = random.randint(1,8)
#         if (x1 != x6 or y1 != y6) and (x2 != x6 or y2 != y6) and (x5 != x6 or y5 != y6) and (x3 != x6 or y3!= y6):
#             map[x6][y6] = 'W'
#             break
#     while True:         # create wall 3 (7)
#         x7 = random.randint(1,8)
#         y7 = random.randint(1,8)
#         if (x1 != x7 or y1 != y7) and (x2 != x7 or y2 != y7) and (x5 != x7 or y5 != y7)and(x3 != x7 or y3!= y7):
#             map[x7][y7] = 'W'
#             break
#     while True:         # create wall 4 (8)
#         x8 = random.randint(1,8)
#         y8 = random.randint(1,8)
#         if (x1 != x8 or y1 != y8) and (x2 != x8 or y2 != y8) and (x5 != x8 or y5 != y8)and(x3 != x8 or y3!= y8):
#             map[x8][y8] = 'W'
#             break
#     while True:         # create wall 5 (9)
#         x9 = random.randint(1,8)
#         y9 = random.randint(1,8)
#         if (x1 != x9 or y1 != y9) and (x2 != x9 or y2 != y9) and (x5 != x9 or y5 != y9)and(x3 != x9 or y3!= y9):
#             map[x9][y9] = 'W'
#             break
#     pmap1()
#     key = 0
#     prefx = x1
#     prefy = y1
#     print('LEVEL '+ str(level))
#     print('Freeplay! It is only getting harder and harder...')
#     if level == 7:
#         print('New Ability: Wallpass')
#         print('You can pass through all walls with this ability!')
#         print('Only works for 1 floor, can be used 3 times per game.')
#         print('Press F to activate it during movement phase.')
#     if level == 8:
#         print('New items! X Attack, X Defense and Distraction Flame!')
#         print('Obtain randomly in the dungeon.')
#         print('Press Q for using X Attack, E for X Defense and X for Distraction Flame!')
#     while True:  # basic movement controls
#         monster['curHP'] = monster['HP']
#         monster['curdamage'] = monster['damage']
#         monster['curdefense'] = monster['defense']
#         hero['curdamage'] = hero['damage']
#         hero['curdefense'] = hero['defense']
#         move = input('Your move? ')
#         if move == 'w':
#             if x1 != 0:
#                 map[x1][y1] = '-'
#                 x1 -=1
#                 map[x1][y1] = 'H'
#         elif move == 'a':
#             if y1 != 0:
#                 map[x1][y1] = '-'
#                 y1 -=1
#                 map[x1][y1] = 'H'
#         elif move == 's':
#             if x1 != 9:
#                 map[x1][y1] = '-'
#                 x1 +=1
#                 map[x1][y1] = 'H'
#         elif move == 'd':
#             if y1 != 9:
#                 map[x1][y1] = '-'
#                 y1 +=1
#                 map[x1][y1] = 'H'
#         elif move == 'c':
#             print('sneaky arent you?')
#             break
#         elif move == 'e':
#             print('sword: '+str(equip['sword']))
#             print('shield: '+str(equip['shield']))
#             print('armor: '+str(equip['armor']))
#             print('boots: '+str(equip['boots']))
#             print('X Attack: ' + str(xatk))
#             print('X Defense: ' + str(xdef))
#             print('Distraction Flame: ' + str(distr))
#         elif move =='f':

#             x4 = y4 = x6 = y6 = x7 = y7 = x8 = y8 = x9 = y9 = 0
#             print('Use a Wall Pass!')
#         else:
#             print('invalid')
#         if (x1 == x2 and y1 == y2) or (x1 == x5 and y1 == y5):
#             print('you just obtained a key')
#             key += 1
#         if x1 == x3 and y1 == y3:
#             if key <2:
#                 print('you need to obtain a key first')
#             else:
#                 print('you finished lvl ' + str(level))
#                 break
#         if prefx == x3 and prefy == y3:
#             map[x3][y3] = 'D'
#         if (x1 == x4 and y1 == y4) or (x1 == x6 and y1 == y6) or (x1 == x7 and y1 == y7) or (x1 == x8 and y1 == y8) or (x1 == x9 and y1 == y9):
#             print('you cant walk though walls, this isnt a magic game')
#             x1 = prefx
#             y1 = prefy
#             map[x1][y1] = 'H'
#             map[x4][y4] = 'W'
#             map[x6][y6] = 'W'
#             map[x7][y7] = 'W'
#         if monscount < monsmax:
#             mons = random.random()
#             monster['HP'] = monster['baseHP'] + random.randint(-3,3)
#             monster['damage'] = monster['basedamage'] + random.randint(-2,2)
#             monster['defense'] = monster['basedefense'] + random.randint(-2,2)
#             if mons <= monster['rate'] and move != 'e' and move != 'f':
#                 print('Encountered a monster!')
#                 while monster['curHP'] >0 and hero['curHP'] >0:
#                     print('HP: '+str(hero['curHP'])+ '     Monster HP: '+str(monster['curHP'])),
#                     while True:
#                         moncrit = 0
#                         hcrit = 0
#                         action = input('choose your move: ')
#                         if action == 'atk' or action == '1':
#                             crit = random.randint(1,100)
#                             critm = random.randint(1,100)
#                             if hero['crirate'] >= crit:
#                                 hero['curdamage'] = hero['curdamage'] * hero['cridmg']
#                             if monster['crirate'] >= critm:
#                                 monster['curdamage'] = monster['curdamage'] * monster['cridmg']
#                             if hero['curstack'] > 0:
#                                 dmg = hero['curdamage'] - monster['curdefense']
#                                 if dmg<=0:
#                                     dmg = 1
#                                 monster['curHP'] = math.floor(monster['curHP'] - dmg) 
#                                 print('Hero dealt '+ str(dmg)+' damage!'
#                                 # if hcrit == 1:

#                                 hero['curstack'] -=1
#                             else:
#                                 print('No energy left for attack!')
#                             if hero['crirate'] >= crit:
#                                 hero['curdamage'] = hero['curdamage'] / hero['cridmg']
#                                 hcrit += 1
#                             if monster['crirate'] >= critm:
#                                 monster['curdamage'] = monster['curdamage'] / monster['cridmg']
#                                 moncrit += 1
#                             break
#                         elif action == 'def' or action =='2':
#                             hero['curdefense'] = math.floor(hero['defense'] *1.5)
#                             hero['curstack'] += 1
#                             break
#                         elif action == 'run' or action == '3':
#                             fleee = random.random()
#                             if fleee <= (hero['flee'] - monster['flee']):
#                                 yaaay == 1
#                                 print('Got away safely!')
#                                 break
#                             else:
#                                 print('Cant escape!')
#                                 hero['curstack'] += 1
#                                 break
#                         elif action == 'q':
#                             if xatk > 0:
#                                 hero['curdamage'] *= 2
#                                 xatk -= 1
#                                 print('Used X Attack!')
#                             else:
#                                 print('No X Attack left!')
#                         elif action == 'e':
#                             if xdef > 0:
#                                 hero['curdefense'] *= 2
#                                 xdef -= 1
#                                 print('Used X Defense!')
#                             else:
#                                 print('No X Defense left!')
#                         elif action == 'x':
#                             if distr > 0:
#                                 distr -= 1
#                                 print('Used Distraction Flame!')
#                                 break
#                             else:
#                                 print('No Distraction Flame left!')
#                     if action =='run' or action == '3' or action =='x':
#                         break
#                     dmg = math.floor(monster['curdamage'] - hero['curdefense'])
#                     if dmg <=0:
#                         dmg = 1
#                     hero['curHP'] = math.floor(hero['curHP'] - dmg)
#                     print('Monster dealt '+ str(dmg)+' damage!')
#                     if moncrit = 1:
#                         print('A critical hit!')
#                     hero['curdefense'] = hero['defense']
#                 if monster['curHP']<=0:
#                     print('Monster have been defeated!')
#                     monscount += 1
#                 elif hero['curHP'] <=0:
#                     herodefeat = 1
#                     print('You have been defeated.')
#                     break
#         if hpcount <hpboxmax and move != 'e':
#             hprand = random.random()
#             if hprand <= monster['HPbox']:
#                 print('Got a HP box!')
#                 hero['curHP'] = hero['HP']
#                 hpcount += 1
#         if ((xx1 == x1 and yy1 == y1) or (xx2 == x1 and yy2 == y1) or (xx3 == x1 and yy3 == y1) or (xx4 == x1 and yy4 == y1) or (xx5 == x1 and yy5 == y1) or (x0 == x1 and y0 == y1)) and level >= 8:
#             whatitem = random.randint(1,4)
#             if equipco < 2:
#                 if whatitem ==1:
#                     if equip['sword'] == 0:
#                         hero['damage'] += 1
#                         hero['curdamage'] += 1
#                         print('Got a sword!')
#                         equip['sword'] +=1
#                     else:
#                         hero['damage'] += 1
#                         hero['curdamage'] += 1
#                         print('Sword upgraded!')
#                         equip['sword'] +=1
#                 elif whatitem ==2:
#                     if equip['shield'] == 0:
#                         hero['defense'] += 1
#                         hero['curdefense'] += 1
#                         print('Got a shield!')
#                         equip['shield'] +=1
#                     else:
#                         hero['defense'] += 1
#                         hero['curdefense'] += 1
#                         print('Shield upgraded!')
#                         equip['shield'] +=1
#                 elif whatitem ==3:
#                     if equip['armor'] == 0:
#                         hero['HP'] += 3
#                         hero['curHP'] += 1
#                         print('Got an armor!')
#                         equip['armor'] +=1
#                     else:
#                         hero['HP'] += 3
#                         hero['curHP'] += 3
#                         print('Armor upgraded!')
#                         equip['curHP'] +=1    
#                 else:
#                     if equip['boots'] == 0:
#                         hero['flee'] += 0.1
#                         print('Got boots!')
#                         equip['sword'] +=1
#                     else:
#                         hero['flee'] += 0.1
#                         print('Boots upgraded!')
#                         equip['boots'] +=1
#                 equipco += 1
#         if icount < imax:
#             iok = random.random()
#             if iok <= 0.1:
#                 whatbattle = random.randint(1,10)
#                 if whatbattle < 5:
#                     print('Got a X Attack!')
#                     xatk += 1
#                 elif whatbattle <9:
#                     print('Got a X Defense!')
#                     xdef += 1
#                 else:
#                     print('Got a Distraction Flame!')
#                     distr += 1
#         prefx = x1
#         prefy = y1
#         pmap1()
#         print('HP: ', str(hero['curHP']))
#         hero['curstack'] += 1
#     if herodefeat == 1:
#         break