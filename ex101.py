from datetime import date


def voto(idade):
	if idade < 16:
		return 'NEGADO'
	elif 16 <= idade < 18 or idade > 65:
		return 'OPCIONAL'
	else:
		return 'OBRIGATÓRO'


nasc = int(input('Em que ano você nasceu? '))
suaidade = date.today().year - nasc
print(f'Com {suaidade} anos: VOTO {voto(suaidade)}.')
