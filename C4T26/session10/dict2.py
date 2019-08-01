employees = [
    {
    'name': 'Huy',
    'role': 'Waiter',
    'hours': 12,
    'salary per hr ($)' : 0.8
    },
    {
        'name': 'Tung',
        'role': 'Cook',
        'hours': 24,
        'salary per hr ($)' : 1.5
    },
    {
        'name': 'M.Duc',
        'role': 'Manager',
        'hours': 20,
        'salary per hr ($)' : 2
    }
]
# a = input('Name: ')
# b = input('role: ')
# c = input('hours: ')
# d = input('salary per hr($): ')
# p4 = {
#     'name': a,
#     'role': b,
#     'hours': c,
#     'salary per hr($)': d,
# }
# employees.append(p4)
# a = input('Name: ')
# b = input('role: ')
# c = input('hours: ')
# d = input('salary per hr($): ')
# p5 = {
#     'name': a,
#     'role': b,
#     'hours': c,
#     'salary per hr($)': d,
# }
# employees.append(p5)
employees[0] = {
    'name': 'Huyen',
    'role': 'Waitress',
    'hours': 14,
    'salary per hr ($)': 1
}

# employees.pop(len(employees)-1)
a = []
for i in employees:
    print(i['salary per hr ($)'])
    a.append(i['salary per hr ($)']*i['hours']*20)
print(a)
for j in range(0,len(a),1):
    print('luong thang cua '+employees[j]['name']+' la '+str(a[j])+'$')
k = sum(a)
print('tong so tien: '+str(k)+'$')
