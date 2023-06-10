jogador = dict()
jogador['nome'] = str(input('Nome do Jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
jogador['gols'] = []
total_gols = 0
for i in range(0, jogador['partidas']):
    jogador['gols'].append(int(input(f'Quantos gols na partida {i}? ')))
    total_gols += jogador['gols'][i]
jogador['total'] = total_gols
print('-='*15)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-='*15)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'\t=> Na partida {i}, fez {v} gols.')
print(f'Foram um total de {jogador["total"]} gols')
