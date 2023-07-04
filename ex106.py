def titulo(txt):
	larg = len(txt) + 4
	print('~'*larg)
	print(f'{txt:^{larg}}')
	print('~'*larg)


while True:
	titulo('SISTEMA DE AJUDA PyHELP')
	duvida = input('Função ou Biblioteca > ')
	if duvida in 'FIMfim':
		break
	print(help(duvida))
