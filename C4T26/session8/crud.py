things = ['a','b','c']
item = input('new item:')
things.append(item)
print(things, sep='| ')
print(*things, sep ='| ') #ngan cach cac phan tu trong list
print(things[-1].upper())
x = input('delete thing: ')
if things.count(x) >0:
    things.remove(x)
else:
    print(x+' do not exist')
y = int(input('delete number: '))
if len(things) < y:
    print('do not exist')
else:
    things.pop(y)
for i, value in enumerate(things):
    print(i, value)       #PRINT RA MOT LIST CO DANH SO
for i in things:
    print(i.upper(), end=" ")