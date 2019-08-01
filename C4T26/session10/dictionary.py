dictionary = {
    'a' : 1,
    'b' : 'aaa',
}
dictionary[input('key: ')] = input('value: ')
dictionary['a'] = 2
print(dictionary)
del dictionary['b']
print(dictionary)
print(dictionary[input('key: ')])
a = input('check key: ') in dictionary
print(a)