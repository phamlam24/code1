import random
listword = ['apple','banana','cat','dog','ear','fanatic', "abcdefghjkmnou"]
word = listword[random.randint(0,len(listword)) -1]
characters = list(word)
for i in range(1,30):
    place1 = random.randint(0, len(word)) - 1
    place2 = random.randint(0, len(word)) - 1
    placeholder = characters[place1]
    characters[place1] = characters[place2]
    characters[place2] = placeholder
for j in characters:
    print(j,end='')
print()
check = input('Enter the word: ')
if check == word:
    print('correct')
else:
    print('wrong')

