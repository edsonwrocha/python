r = float(input('Digite uma quantia em reais: '))
d = r / 3.27
print('É essa quantia de \033[32mR${}\033[m equivale a \033[32mU${:.2f}\033[m na cotação de hoje'.format(r, d))
