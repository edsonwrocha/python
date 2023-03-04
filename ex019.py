import random
print('Vamos sortear um aluno em quatro: ')
continuar = 1
lista = []
lista.append(input('Digite o nome do primeiro aluno:'))
lista.append(input('Digite o nome do segundo: '))
lista.append(input('Digite o nome do terceiro: '))
lista.append(input('Digite o nome do quarto: '))
while continuar:
    print('O aluno sorteado foi \033[7;32m{}\033[m'.format(random.choice(lista)))
    continuar = int(input('Deseja sortear novamente: Sim digite 1, não digite 0: '))

