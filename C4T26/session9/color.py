from turtle import *
colors = ['red', 'blue', 'green']
while True:
    option = input('function: ')
    if option == 'add':
        adder = input('color: ')
        colors.append(adder)
        print(colors)
    elif option == 'view':
        view = int(input('enter position: '))
        print(colors[view - 1])
        print(colors)
    elif option == 'delete':
        dele = input('place or name: ')
        x = dele.isdigit()
        if x == True:
            colors.pop(int(dele))
        else:
            colors.remove(dele)
        print(colors)
    elif option == 'draw':
        for i in range(0,len(colors)):
            pencolor(colors[i])
            forward(30)
    else:
        break
mainloop()
