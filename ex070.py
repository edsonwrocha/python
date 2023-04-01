menor = 0
prod_menor = 0
mais_1000 = 0
total = 0
print('_'*10, 'Caixa Eletrônico V1.0', '_'*10)
while True:
    print('+='*20)
    produto = str(input('Nome do produto: '))
    while True:
        preco = str(input('Preço: R$')).strip()
        if preco.isnumeric():
            preco = float(preco)
            if preco > 1000:
                mais_1000 += 1
            total += preco
            break
        else:
            print('Erro, digite um preço válido!')
    if menor == 0:
        menor = preco
        prod_menor = produto
    elif preco < menor:
        menor = preco
        prod_menor = produto
    while True:
        continuar = str(input('Quer continuar: [S/N]')).strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('Erro, digite uma opção correta!')
    if continuar == 'N':
        break
print('+='*5, 'FIM DO PROGRAMA', '+='*5)
print(f'O total de compras foi R${total}')
print(f'Temos {mais_1000} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {prod_menor} e custou R${menor}')
