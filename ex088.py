from random import randint
from time import sleep
palpites = []
jogo = []
sorteio = 0
print('SORTEIO MEGA SENA')
while True:
    qtd = int(input('Digite quantos jogos da Mega Sena você quer sortear: '))
    if qtd != 0:
        break
    else:
        print('Tente novamente! Digite um número válido.')
for num in range(0, qtd):
    for i in range(0, 6):
        while True:
            sorteio = randint(1, 60)
            if sorteio not in jogo:
                jogo.append(sorteio)
                break
    palpites.append(jogo[:])
    jogo.clear()
    sleep(1)
    print(f'Jogo {num+1}: {sorted(palpites[num])}')
sleep(1)
