print('BANCO CEV')
ced_50 = ced_20 = ced_10 = ced_1 = 0
while True:
    total = int(input('Digite o valor a ser sacado: R$'))
    if total != 0:
        break
    else:
        print('Digite um valor válido!')
while total != 0:
    while total > 49:
        ced_50 += 1
        total -= 50
    if ced_50 > 0:
        print(f'O total de {ced_50} cédulas de R$50')
    while total > 19:
        ced_20 += 1
        total -= 20
    if ced_20 > 0:
        print(f'O total de {ced_20} cédulas de R$20')
    while total > 9:
        ced_10 += 1
        total -= 10
    if ced_10 > 0:
        print(f'O total de {ced_10} cédulas de R$10')
    while total > 0:
        ced_1 += 1
        total -= 1
    if ced_1 > 0:
        print(f'O total de {ced_1} cédulas de R$1')
print('FIM DO PROGRAMA')