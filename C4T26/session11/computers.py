computers = {
    'hp' : 20,
    'dell' : 50,
    'macbook' : 12,
    'asus' : 30,
}
computers['toshiba'] = 10
computers[input('hang: ')] = int(input('so hang: '))
computers['dell'] += 10
computers['macbook'] = 2
computers['fujitsu'] = 15
computers['alienware'] = 5
print('tong so hang: '+ str(sum(computers.values())))
print(computers[input('xem luong hang con lai: ')])

prices = {
    'hp': 600,
    'dell': 650,
    'macbook': 12000,
    'asus': 400,
    'acer': 350,
    'toshiba': 600,
    'fujitsu': 900,
    'alienware': 1000,
}
print(prices[input('nhap hang: ')])

while True:
    types = input('loai may: ')
    number = int(input('so luong may: '))
    if number > computers[types]:
        print('invalid')
        break
    else:
        bill = prices[types] * number
        print('gia tien: '+str(bill))
        computers[types] -= number
    print(computers)

hang = input('nhap hang: ')
print('tong gia tri la: '+str(computers[hang]*prices[hang]))

giatri = []
for i in computers.keys():
    giatri.append(computers[i]*prices[i])
print(sum(giatri))
        