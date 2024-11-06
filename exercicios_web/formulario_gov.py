print('Formulário cadastro único')
print('=========================')
nome = str(input('Nome: '))
idade = int(input('Idade: '))
sal = float(input('Salário: '))
sexo = str(input('Sexo: [M/F] '))
estCivil = str(input('Estado civil: '))
nomeconf = 'ana'
conf_nome = nome.__len__() > nomeconf.__len__()
conf_idade = (idade > 0) and (idade < 150)
conf_sal = sal > 0
conf_sexo = sexo == 'm' or sexo == 'f'
conf_civil = estCivil == 's' or estCivil == 'c' or estCivil == 'v' or estCivil == 'd'
confere = (conf_nome is True) and (conf_idade is True) and (conf_sal is True) and (conf_civil is True)
while confere == False:
    if confere == False and confere != True:
        print('Formulário cadastro único')
        print('=========================')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        sal = float(input('Salário: '))
        sexo = str(input('Sexo: [M/F] '))
        estCivil = str(input('Estado civil: [s/c/v/d] '))
    elif confere == True:
        ''
    conf_nome = nome.__len__() > nomeconf.__len__()
    conf_idade = (idade > 0) and (idade < 150)
    conf_sal = sal > 0
    conf_sexo = sexo == 'm' or sexo == 'f'
    conf_civil = estCivil == 's' or estCivil == 'c' or estCivil == 'v' or estCivil == 'd'
    confere = (conf_nome is True) and (conf_idade is True) and (conf_sal is True) and (conf_civil is True)
print('Usuário cadastrado com sucesso!')