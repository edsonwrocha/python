from time import sleep
def maior(*numeros):
	print('-='*30)
	qtd = len(numeros)
	maior = numeros[0]
	print('Analisando os valores passados...')
	for i in numeros:
		print(i, end=' ', flush=True)
		sleep(0.25)
		if i > maior:
			maior = i
	print(f'Foram informados {qtd} valores ao todo.')
	print(f'O maior valor informado foi {maior}')


maior(2, 4, 9, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
