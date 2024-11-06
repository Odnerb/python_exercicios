print('------------------------')
print('CAMPEONATO CARIOCA: 2023')
print('------------------------')
i = 0
time = []
while i < 4:
    i = i + 1
    clube = input(f'Diga o nome do {i}º time: ')
    time.append(clube)
c = 0
print('-----------------------')
while c < 4:
    if (c == 0):
        print(f'{time[0]:10} [] x [] {time[1]}')
        print(f'{time[0]:10} [] x [] {time[2]}')
        print(f'{time[0]:10} [] x [] {time[3]}')
    elif (c == 1):
        print(f'{time[1]:10} [] x [] {time[0]}')
        print(f'{time[1]:10} [] x [] {time[2]}')
        print(f'{time[1]:10} [] x [] {time[3]}')
    elif (c == 2):
        print(f'{time[2]:10} [] x [] {time[0]}')
        print(f'{time[2]:10} [] x [] {time[1]}')
        print(f'{time[2]:10} [] x [] {time[3]}')
    else:
        print(f'{time[3]:10} [] x [] {time[0]}')
        print(f'{time[3]:10} [] x [] {time[1]}')
        print(f'{time[3]:10} [] x [] {time[2]}')
    c = c + 1