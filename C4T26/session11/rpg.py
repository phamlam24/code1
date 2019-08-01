import random
character = {
    'name': 'Light',
    'age': 17,
    'strength': 8,
    'defense':10,
    'HP':100,
    'backpack': ['Shield','Bread Loaf'],
    'gold': 100,
    'level': 2
}
character['gold'] += 50
character['backpack'].append('FlintStone')
character['Pocket'] = ['MonsterDex','Flashlight']

moveset =[
    {
        'name':'Tackle',
        'minimum level':1,
        'damage':5,
        'hit rate':0.3,
    },
        {
        'name':'Quick Attack',
        'minimum level':2,
        'damage':3,
        'hit rate':0.5,
    },
        {
        'name':'Strong Kick',
        'minimum level':4,
        'damage':9,
        'hit rate':0.2,
    }
]
for i, value in enumerate(moveset):
    print(str(i+1)+'.',value['name'])
atk = int(input('Choose your attack: ')) -1
if moveset[atk]['minimum level'] > character['level']:
    print('Level not enough!')
else:
    hitormiss = random.random()
    if hitormiss >= moveset[atk]['hit rate']:
        print(character['name']+' dealt '+str(moveset[atk]['damage'])+' damage!')
    else:
        print('Miss!')