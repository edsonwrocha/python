num_ext = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    while True:
        num = int(input('Digite um número de 0 a 20 e mostrarei ele por extenso: '))
        if num >= 0 and num <= 20:
            break
        else:
            print('Tente novamente.', end=' ')
    print(f'{num} por extenso é {num_ext[num]}')
    while True:
        cont = input('Você quer continuar? [S/N]: ').upper().strip()[0]
        if cont in 'NS':
            break
    if cont == 'N':
        break
