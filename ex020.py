import random
print('Vamos sortear a ordem de apresentação do trabalho: ')
continuar = 1
lista = []
lista.append(input('Digite o nome do primeiro aluno:'))
lista.append(input('Digite o nome do segundo: '))
lista.append(input('Digite o nome do terceiro: '))
lista.append(input('Digite o nome do quarto: '))
while continuar:
    print('A ordem de apresentação será: {}'.format(random.sample(lista, 4)))
    continuar = int(input('Deseja sortear novamente: Sim digite 1, não digite 0: '))
