lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        cont = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if cont in 'SN':
            break
    if cont == 'N':
        break
print('-='*30)
print(f'Você digitou {len(lista)} números')
print(f'Os números digitados em ordem descrescente é : {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 foi digitado e está na lista!')
else:
    print('O valor 5 não foi digitado e não se encontra na lista!')
