names = ['Ivan', 'Sasha', 'Renat']
match names:
    case ['Ivan', _, 'Renat']:
         print('We have Ivan and Renat')
    case [_, _, 'Renat']:
         print('We have only Renat')
    case _:
         print('We have no one')