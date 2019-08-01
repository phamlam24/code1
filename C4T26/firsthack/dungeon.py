import random
import math
swlvl = 0
shlvl = 0
arlvl = 0
bolvl = 0
map =[]
def pmap():
    for i in range(6):
        for j in range(6):
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
    if (x1 != x6 or y1 != y6) and (x2 != x6 or y2 != y6) and (x5 != x6 or y5 != y6):
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
    
}
monster = {
    'HP' : 10,
    'damage': 6,
    'reload': 2,
    'stack': 1,
    'defense': 5,
    'flee': 0.7,
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
    if (x1 != x6 or y1 != y6) and (x2 != x6 or y2 != y6) and (x5 != x6 or y5 != y6):
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
                    if fleee >= monster['flee']:
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
monster['HP'] +=1
monster['HPbox'] = 0.05
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
    if (x1 != x6 or y1 != y6) and (x2 != x6 or y2 != y6) and (x5 != x6 or y5 != y6):
        map[x6][y6] = 'W'
        break
while True:         # create wall 3 (7)
    x7 = random.randint(0,5)
    y7 = random.randint(0,5)
    if (x1 != x7 or y1 != y7) and (x2 != x7 or y2 != y7) and (x5 != x7 or y5 != y7):
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
    prefx = x1
    prefy = y1
    pmap()
    print('HP: ', str(hero['curHP']))

#                           LEVEL 5:
monster['defense'] += 1
monster['attack'] += 1

monsmax = 5
monscount = 0
icount = 0
hpboxmax = 2
hpcount = 0
equipmax = 3
equip = 0
equiprate = 0.1
equipment = {
    'sword':'none',
    'shield':'none',
    'armor':'none',
    'boots':'none'
}
swords =[
    ['wooden',1,5],
    ['bronze',2,6],
    ['silver',3,7],
    ['golden',4,8],
    ['crystal',5,10],
    ['diamond',6,12],
    ['legend',7,15],
    ['unknown',10,20]
] #30%
shields = [
    ['wooden',1,5],
    ['bronze',2,6],
    ['golden',3,8],
    ['diamond',4,10],
    ['captain',5,15]
] #20%
armor = [
    ['basic',1,5],
    ['chain',3,6],
    ['iron',5,7],
    ['golden',8,9],
    ['diamond',10,12],
    ['unbeatable',20,15],
    ['bedrock',35,20]
] #40%
boots = [
    ['basic',0.05,5],
    ['feather',0.15,7],
    ['lightspeed',0.35,10],
    ['hermes',0.75,17]
] #10%
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
    if (x1 != x6 or y1 != y6) and (x2 != x6 or y2 != y6) and (x5 != x6 or y5 != y6):
        map[x6][y6] = 'W'
        break
while True:         # create wall 3 (7)
    x7 = random.randint(0,5)
    y7 = random.randint(0,5)
    if (x1 != x7 or y1 != y7) and (x2 != x7 or y2 != y7) and (x5 != x7 or y5 != y7):
        map[x7][y7] = 'W'
        break
pmap()
key = 0
prefx = x1
prefy = y1
print('LEVEL 5')
print('Inventory unlocked! Press E to see and E again to exit.')
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
        print('sword: '+ equipment['sword'])
        print('shield: '+ equipment['shield'])
        print('armor: '+ equipment['armor'])
        print('boots: '+ equipment['boots'])
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
    if equip < equipmax:
        chance = random.random()
        if chance <= 0.1:
            typing = random.random()
            if typing <=0.1:

    prefx = x1
    prefy = y1
    pmap()
    print('HP: ', str(hero['curHP']))