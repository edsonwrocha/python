from random import randint
tentativas = 1
num = randint(0, 10)
print('Estou pensando em um número, tente adivinhar!')
user = int(input('Digite um número inteiro de 0 até 10: '))

while user != num:
    if user < num:
        print('Mais... Tente novamente!')
    elif user > num:
        print('Menos... Tente novamente!')
    user = int(input('Digite outro número de 0 a 10: '))
    tentativas += 1
print('Você acertou!')
print('Número de tentativas: {}'.format(tentativas))