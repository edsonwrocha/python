from time import sleep

def contador(c, f, p):
	if p == 0:
		p = 1
	elif p < 0:
		p *= (-1)
	if c < f:
		while c <= f:
			print(c, end=' ', flush=True)
			sleep(1)
			c += p
		print('FIM!')
		sleep(1)
	elif c > f:
		while c >= f:
			print(c, end=' ', flush=True)
			sleep(1)
			c -= p
		print('FIM!')
		sleep(1)
	else:
		print('ERRO, Início = ao FIM, tente novamente')


print('=-'*20)
print('Contagem de 1 até 10 de 1 em 1')
contador(1, 10, 1)
print('=-'*20)
print('Contador de 10 até 0 de 2 em 2')
contador(10, 0, 2)
print('=-'*20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('=-'*20)
contador(inicio, fim, passo)
