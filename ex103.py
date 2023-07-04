def ficha(nome = '', gols=''):
	if nome == '':
		nome = '<desconhecido>'
	if gols == '':
		gols = 0
	print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


ficha(input('Nome do jogador: '), input('Número de gols: '))
