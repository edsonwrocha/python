from random import randint
from time import sleep
from operator import itemgetter
jogo = dict()
for i in range(1, 5):
    jogo[f'jogaodor{i}'] = randint(1, 6)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
