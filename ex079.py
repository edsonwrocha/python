lista = []
while True:
    entrada = int(input('Digite um valor: '))
    if entrada not in lista:
        lista.append(entrada)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if cont in 'SN':
            break
    if cont == 'N':
        break
print('-='*30)
print(f'Você digitou os valores {sorted(lista)}')
