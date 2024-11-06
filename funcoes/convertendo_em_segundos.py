# Programa que recebe três números inteiros como parâmetros que
# representam: horas, minutos e segundos, e os converte em segundos

def hora_segundos(h, m, s):
    if h < 24 and m < 60 and s < 60:
        conversao = (60*60*h)+(60*m)+s
        return conversao
    else:
        print(f'Hora inválida, digite novamente\nA hora certa!')
        return hora_agora()


def hora_agora(fun=hora_segundos):
    horas = int(input('Hora: '))
    minutos = int(input('Minutos: '))
    segundos = int(input('Segundos: '))
    return fun(horas, minutos, segundos)


print('---------------------------------')
print(f'{hora_agora()} s')

