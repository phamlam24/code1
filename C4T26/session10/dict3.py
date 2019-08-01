rand = {
    'name': 'random',
    'year': 2018,
    'characters': ['a','b','c','d']
}
rand['country'] = 'earth'
rand['characters'].append('e')
rand['characters'].pop(0)
print(rand['characters'][1])
for i in rand['characters']:
    print(i)
for i,j in rand.items():
    print(i+' - ',j)
