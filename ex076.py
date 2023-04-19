tabela = ('Lápis', 1.75, 'Caderno', 20, 'Caneta', 1.5, 'Mochila', 100, 'Calça', 301.50, 'Piloto', 8.75)
print('_'*60)
titulo = 'LISTAGEM DE PREÇOS'
print(f'{titulo:^60}')
print('_'*60)
for i in range(0, len(tabela), 2):
    print(f'{tabela[i]:.<51}R${tabela[i+1]:>7.2f}')
print('_'*60)
