from random import randint
from time import sleep
ranking = []
jogo = dict()
for i in range(1, 5):
    jogo[f'jogador{i}'] = randint(1, 6)
    print(f'\tO jogador{i} tirou {jogo[f"jogador{i}"]}')
    sleep(1)
ranking = set(sorted(jogo.values(), reverse=True))
posicao = 1
print('O Ranking dos jogadores:')
for i in ranking:
    for jogador, dado in jogo.items():
        if dado == i:
            print(f'\t{posicao}° lugar: {jogador} com {dado}')
            sleep(1)
            posicao += 1
