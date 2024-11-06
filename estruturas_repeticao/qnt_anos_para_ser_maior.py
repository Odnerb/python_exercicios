altChico = 1.50
altZe = 1.10
anos = 0
while altChico > altZe:
    anos = anos + 1
    altChico = altChico + 0.02
    altZe = altZe + 0.03
print('========================================')
print(f'Zé será maior que Carlos em {anos} anos')
print(f'Altura Chico: {altChico:.2f}')
print(f'Altura Zé: {altZe:.2f}')
print('========================================')
