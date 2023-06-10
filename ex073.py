brasileirao = ('Fluminense', 'Flamengo', 'Atlético-PR', 'Palmeiras', 'Botafogo',
               'Bragantino', 'Corinthians', 'Vasco da Gama', 'Grêmio', 'Internacional',
               'Fortaleza', 'Bahia', 'Cruzeiro', 'São Paulo', 'Atlético-MG',
               'Cuiabá', 'Santos', 'Goiás', 'América-MG', 'Coritiba')
print('Os 5 primeiros colocados do brasileirão são: ', end='')
print(brasileirao[0:5])
print('Os 4 últimos colocados são: ', end='')
print(brasileirao[16:])
print('Times que jogam o brasileirão em ordem alfabética: ')
print(sorted(brasileirao))
if 'Chapecoense' in brasileirao:
    print('O Chapecoense está na posição {}ª'.format(brasileirao.index('Chapecoense')+1))
else:
    print('O Chapecoense não está jogando a série A do Brasileirão 2023')
