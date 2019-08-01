questions =[
    {
        'question': '1+1 =?',
        'ans1':'1. 1',
        'ans2': '2. 2',
        'ans3': '3. 3',
        'ans4': '4. 69',
        'correct': 2
    },
    {
        'question': '2+2 = ?',
        'ans1':'1. 9',
        'ans2': '2. 5',
        'ans3': '3. 4',
        'ans4': '4. infinity',
        'correct': 3
    }
]
goods = 0
for i in questions:
    question = i
    print(question['question'])
    print(question['ans1'])
    print(question['ans2'])
    print(question['ans3'])
    print(question['ans4'])
    ans = int(input('Enter answer: '))
    if ans == question['correct']:
        print('correct')
        goods +=1
    else:
        print('wrong')
percentage = goods / len(questions) *100
print('correct answers: '+str(goods))
print('percentage: '+str(percentage)+'%')