def fatorial(num = 1, show = False):
	"""
	-> Calcula o fatorial de um número.
	:param num: O número a ser calculado.
	:param show: (opcional) Mostrar ou não a conta.
	:return: O valor do Fatorial de um número n.
	"""
	f = 1
	for i in range(num, 0, -1):
		f *= i
		if show:
			if i > 1:
				print(i, end=' x ')
			else:
				print(f'{i} = ', end='')
	return f


print(fatorial(5))
print(fatorial(5, show = True))
help(fatorial)
