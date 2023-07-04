def contador(i, f, p):
	"""
	->Função que recebe inicio, fim e passo de uma sequência e a imprimi na tela
	:param i: inicio da contagem
	:param f: fim da contagem
	:param p: passo da contagem
	:return: sem retorno
	"""
	c = 1
	while c <= f:
		print(f'{c}', end='..')
		c += p
	print('FIM!')


contador(1, 10, 1)
help(contador)
