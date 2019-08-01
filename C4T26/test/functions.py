def function_1():
    print('hello')
function_1()

def function_2(a):
    print('hello ' + a)
x = input('Name? ')
function_2(x)

def return_1(a):
    return 3+a
x = return_1(7)
print(return_1(5))
print(x)