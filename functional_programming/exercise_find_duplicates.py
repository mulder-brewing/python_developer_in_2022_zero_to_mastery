some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

print(list({letter for letter in some_list if some_list.count(letter) > 1}))
