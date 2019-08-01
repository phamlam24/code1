highscore = [100,89,95,77]
for i, score in enumerate(highscore):
    xxxx = i+1
    print(str(xxxx)+".", score)
while True:
    a = int(input('enter new score'))
    highscore.append(a)
    highscore.sort(reverse=True)
    if len(highscore)>5:
        highscore.pop(5)
    for i, score in enumerate(highscore):
        xxxx = i+1
        print(str(xxxx)+".", score)