from random import randint
from time import sleep
print('teste')
cores = {
        'verde': '\033[32m',
        'vermelho': '\033[31m',
        'azul': '\033[34m',
        'normal': '\033[m'
        }
computador = randint(1, 3)

usr = int(input("""Vamos jogar JOKENPÔ
1 -PEDRA
2 -PAPEL
3 -TESOURA
Digite sua escolha: """))
print('JO...', end=' ')
sleep(1)
print('KEN...', end=' ')
sleep(1)
print('PÔ!')
sleep(1.5)

### possibilidades: pedra x pedra pedra x papel pedra x tesoura
### papel x pedra papel x papel papel x tesoura
### tesoura x pedra tesoura x papel tesoura x tesoura

if usr == computador:
    print('{}EMPATE!{}'.format(cores['azul'], cores['normal']))
    if usr == 1:
        print('PEDRA VS PEDRA')
    elif usr == 2:
        print('PAPEL VS PAPEL')
    elif usr == 3:
        print('TESOURA VS TESOURA')
elif usr == 1 and computador == 2:
    print('{}GAME OVER!{}'.format(cores['vermelho'], cores['normal']))
    print('PEDRA VS PAPEL - COMPUTADOR VENCEU')
elif usr == 1 and computador == 3:
    print('{}WIN!{}'.format(cores['verde'], cores['normal']))
    print('PEDRA VS TESOURA - VOCÊ GANHOU!')
elif usr == 2 and computador == 1:
    print('{}WIN!{}'.format(cores['verde'], cores['normal']))
    print('PAPEL VS PEDRA - VOCÊ GANHOU!')
elif usr == 2 and computador == 3:
    print('{}GAME OVER!{}'.format(cores['vermelho'], cores['normal']))
    print('PAPEL VS TESOURA - COMPUTADOR VENCEU')
elif usr == 3 and computador == 1:
    print('{}GAME OVER!{}'.format(cores['vermelho'], cores['normal']))
    print('TESOURA VS PEDRA - COMPUTADOR VENCEU')
elif usr == 3 and computador == 2:
    print('{}WIN!{}'.format(cores['verde'], cores['normal']))
    print('TESOURA VS PAPEL - VOCÊ GANHOU')
else:
    print('{}ERRO, TENTE NOVAMENTE{}'.format(cores['vermelho'], cores['normal']))

### FAZER ANIMAÇÃO JOKEEENPOOO COM SLEEP E CORES :3