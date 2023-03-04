preço_inicial = float(input('Digite o preço cheio de um produto: '))
preço_desconto = preço_inicial - (preço_inicial * (5 / 100))
print('O preço desse produto com desconto de 5% é: \033[32mR${}'.format(preço_desconto))
