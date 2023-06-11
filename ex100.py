from random import randint
from time import sleep

numeros = []

def sorteia():
	print('Sorteando 5 valores: ', end=' ', flush=True)
	for i in range(0, 5):
		numeros.append(randint(1, 10))
		sleep(0.25)
		print(numeros[i], end=' ', flush=True)
	print('PRONTO!')
def soma():
	print(f'Somando os valores pares de {numeros}, temos ', end='', flush=True)
	soma = 0
	for i in numeros:
		if i % 2 == 0:
			soma += i
	print(soma)


sorteia()
soma()
