valores = []
pares = []
impares = []

while True:
    valores.append(int(input('Digite um número: ')))
    while True:
        cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if cont in 'SN':
            break
    if cont == 'N':
        break

for i in valores:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print('-+'*20)
print(f'Os números digitados foram {valores}')
print(f'Os números pares digitados foram {pares}')
print(f'Os números impares digitados foram {impares}')
