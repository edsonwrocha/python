from random import randint
from time import sleep

print('=-='*30)
print('Vamos brincar? Vou pensar em um número de 0 a 5, tente adivinhar qual estou pensando')
print('=-='*30)
numero = int(input('Digite a sua alternativa: '))
pensou = randint(0, 5)
print('PROCESSANDO...')
sleep(2)
if numero == pensou:
    print('Parabéns, eu estava pensando no número {}!'.format(pensou))
else:
    print('Sinto muito :/')
    print('Você errou, eu pensei no número {}, tente mais uma vez!'.format(pensou))

