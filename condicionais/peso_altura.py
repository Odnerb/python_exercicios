alt = float(input('Altura (m): '))
peso = float(input('Peso (kg): '))
print('--------------------------------')
print('Classificação de peso')
if alt < 1.20 and peso <= 60:
    print('Classificação: A')
elif ((alt >= 1.20) and (alt <= 1.70)) and peso <= 60:
    print('Classificação: B')
elif (alt > 1.70) and (peso <= 60):
    print('Classificação: C')
elif (alt < 1.20) and ((peso > 60) and peso <= 90):
    print('Classificação: D')
elif ((alt >= 1.20) and (alt <= 1.70)) and ((peso > 60) and peso <= 90):
    print('Classificação: E')
elif (alt > 1.70) and ((peso > 60) and peso <= 90):
    print('Classificação: F')
elif (alt < 1.20) and (peso > 90):
    print('Classificação: G')
elif ((alt >= 1.20) and (alt <= 1.70)) and (peso > 90):
    print('Classificação: H')
elif (alt > 1.70) and (peso > 90):
    print('Classificação: I')
print('--------------------------------')
