from random import randint
pontos = 0
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
while True:
    computador = randint(0, 10)
    user = int(input('Diga um valor (0 até 10): '))
    opcao = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]
    if (user + computador) % 2 == 0 and (user + computador) < 20:
        print(f'Você jogou {user} e o computador jogou {computador}, total de {user + computador} deu PAR')
        print('--' * 15)
    elif (user + computador) % 2 == 1 and (user + computador) < 20:
        print(f'Você jogou {user} e o computador jogou {computador}, total de {user + computador} deu ÍMPAR')
        print('--' * 15)
    if opcao == 'P' and user in range(0, 10):
        if (user + computador) % 2 == 0:
            pontos += 1
            print('Você venceu!')
            print('Vamos jogar novamente')
            print('-=-'* 15)
        else:
            break
    elif opcao == 'I' and user in range(0, 10):
        if (user + computador) % 2 == 1:
            pontos += 1
            print('Você venceu!')
            print('Vamos jogar novamente')
            print('-=-' * 15)
        else:
            break
    else:
        print('Escolha uma opção válida')
print(f'GAME OVER, você ganhou {pontos} vezes')