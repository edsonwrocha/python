print('Banco CEV')
notas_50 = notas_20 = notas_10 = notas_1 = 0
total = int(input('Digite o valor a ser sacado: R$'))
if total // 50 != 0:
    notas_50 = total // 50
    total -= (notas_50 * 50)
    print(f'Total de {notas_50} cédulas de R$50')
if total // 20 != 0:
    notas_20 = total // 20
    total -= (notas_20 * 20)
    print(f'Total de {notas_20} cédulas de R$20')
if total // 10 != 0:
    notas_10 = total // 10
    total -= (notas_10 * 10)
    print(f'Total de {notas_10} cédulas de R$10')
if total // 1 != 0:
    notas_1 = total // 1
    total -= (notas_1 * 1)
    print(f'Total de {notas_1} cédulas de R$1')
print('FIM DO PROGRAMA')
