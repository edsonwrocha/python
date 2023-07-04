def notas(*lista_das_notas, sit=False):
	"""
	-> Função para analisar notas e situações de vários alunos.
	:param lista_das_notas: uma ou mais notas e situações de vários alunos.
	:param sit: valor opcional, indicando se deve ou não adicionar a situação
	:return: dicionário com várias informações sobra a situação da turma
	""" 
	caderneta = dict()
	soma = 0
	caderneta['total'] = len(lista_das_notas)
	for i in lista_das_notas:
		if i == lista_das_notas[0]:
			maior = menor = i
		else:
			if i > maior:
				maior = i
			if i < menor:
				menor = i
		soma += i
	caderneta['maior'] = maior
	caderneta['menor'] = menor
	caderneta['média'] = soma / caderneta['total']
	if sit == True:
		if caderneta['média'] >= 7:
			caderneta['situação'] = 'BOA'
		elif 6 <= caderneta['média'] < 7:
			caderneta['situação'] = 'RAZOÁVEL'
		else:
			caderneta['situação'] = 'PÉSSIMA'
	return(caderneta)


resp = notas(0, 9.5, 6.5, 4, sit=True)
print(resp)
