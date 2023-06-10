from time import sleep

def contador(c, f, p):
	if f < c:
		for i in range(c, f + 1, p):
			print(i, end=' ')
			sleep(0.5)
		print('FIM!')
		sleep(0.5)


print('=-'*20)
print('Contagem de 1 até 10 de 1 em 1')
contador(1, 10, 1)
print('=-'*20)
print('Contador de 10 até 0 de 2 em 2')
contador(10, 0, -2)
