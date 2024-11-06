print('      FACEBOOK       ')
print('------------------------------------')
print('------------------------------------')
user = str(input('Nome usuário: '))
senha = str(input('Senha:         '))
while user == senha:
    if user == senha:
        print('\U0001F6AB Nome de usuário e senha iguais!')
        print('==============================')
        user = str(input('Nome usuário: '))
        senha = str(input('Senha:        '))
    else:
        ''
print('=====================================')
print(f'Seja bem-vindo {user}')
