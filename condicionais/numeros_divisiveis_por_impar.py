print('--------------------')
print('Divisíveis por 3 e 5')
print('--------------------')
num = int(input('Diga um valor: '))
if num % 3 == 0 and not num % 5 == 0:
    print(f'O número {num} é divisível por 3.')
elif num % 5 == 0 and not num % 3 == 0:
    print(f'O número {num} é divisível por 5.')
elif num % 3 == 0 or num % 5 == 0:
    print(f'O número {num} é divisível por 3 e 5\nmas só vale um dos dois!')
elif not num % 3 == 0 or not num % 5 == 0:
    print(f'O valor {num} não é divisível por: 3 e nem 5.')
