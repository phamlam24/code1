i = int(input('nhap thang:'))
if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
    print('31 ngay')
elif i == 2:
    print('28 hoac 29 ngay')
elif i == 4 or i == 6 or i == 9 or i == 11:
    print('30 ngay')
else:
    print('m bi ngu ah')