numlist = [1,2,3,4,5,6]

#     #                       SEARCH
# while True:
#     # good = 0
#     # pos = 0
#     # search = int(input('enter number: '))
#     # for i in range (1,len(numlist)+1,1):
#     #     if search == numlist[i-1]:
#     #         good += 1
#     #         pos = i
#     # if pos>0:
#     #     print('co')
#     #     print('so nay nam o vi tri ' + str(pos))
#     # else:
#     #     print('ko')


print(sum(numlist))
a=0
for i in range (0,len(numlist)):
    a += numlist[i]
print(a)

x = input('enter')
listt = x.split()
listt = list(map(int, listt))   # bien tat ca cac string trong list ve int
placehold = listt
print(listt)
print(sum(listt))

aaaaa = input('enter: ')
even = aaaaa.split(',')
even = list(map(int, even))
for i in range(len(even)-1,-1,-1):
    if even[i] %2 != 0:
        even.pop(i)
print(even)

