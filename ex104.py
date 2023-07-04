def leiaInt(texto):
	while True:
		print(texto, end='')
		dado = input()
		if dado.isnumeric():
			return int(dado)
		else:
			print('ERRO! Digite um número inteiro válido.')


n = leiaInt('Digite um número: ')
print(f'O número digitado foi {n}')
