pessoas = []
cadastro = []
maiorpeso = menorpeso = 0
while True:
    cadastro.append(str(input('Nome: ')))
    cadastro.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maiorpeso = menorpeso =  cadastro[1]
    else:
        if cadastro[1] > maiorpeso:
            maiorpeso = cadastro[1]
        if cadastro[1] < menorpeso:
            menorpeso = cadastro[1]
    pessoas.append(cadastro[:])
    cadastro.clear()
    while True:
        cont = str(input('Quer cadastrar outra pessoa: [S/N] ')).strip().upper()[0]
        if cont in 'SN':
            break
    if cont in 'Nn':
        break
print('-='*30)
print(f'Você cadastrou {len(pessoas)} pessoas!')
print(f'O maior peso foi {maiorpeso}Kg. Peso de ', end='')
for i in range(0, len(pessoas)):
    if pessoas[i][1] == maiorpeso:
        print(f'[{pessoas[i][0]}]', end=' ')
print(f'\nO menor peso foi {menorpeso}Kg. Peso de ', end='')
for i in range(0, len(pessoas)):
    if pessoas[i][1] == menorpeso:
        print(f'[{pessoas[i][0]}]', end=' ')
