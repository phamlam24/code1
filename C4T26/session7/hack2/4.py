from turtle import *
n = int(input('polygon: '))
a = float((n-2)*180/n)
for i in range(1,n+1):
    forward(25)
    left(180-a)
mainloop()