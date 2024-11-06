print("CAIXA D'ÁGUA CILÍNDRICA")
print('Calculo ---------------')
print('=======================')
alt = float(input("Insira a altura da caixa d'água (m): "))
raio = float(input("Insira o raio da caixa d'água (m): "))
pi = 3.141592653589793
vol = pi * (raio**2) * alt
texto_vol = f'{vol:_.2f}'
texto_vol2 = f'{vol * 1000:_.2f}'
# Lembre-se cabeção: replace troca uma letra, palavra, caracter ou símbolo por outros
texto_vol = texto_vol.replace(".",",").replace("_",".")
texto_vol2 = texto_vol2.replace(".",",").replace("_",".")
print('=======================')
print(f"Volume da caixa d'água em m³: {texto_vol}")
print(f"Volume da caixa d'água em l: {texto_vol2}")

