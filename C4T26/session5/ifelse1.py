season = int(input('Enter month'))

if 0 < season<4:
    print('Spring')
elif season<7:
    print('Summer')
elif season<10:
    print("Autumn")
elif season<13:
    print('Winter')
else:
    print('F')