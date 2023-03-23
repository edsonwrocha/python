botao = 0
menu = """
[1]SOMAR
[2]MULTIPLICAR
[3]MAIOR
[4]NOVOS NÚMEROS
[5]SAIR DO PROGRAMA
"""
print('Digite dois números')
num1 = float(input('número 1: '))
num2 = float(input('número 2: '))

while botao != 5:
    print(menu)
    botao = int(input('Digite uma opção: '))
    if botao == 1:
        print('A soma de {} e {} é {}'.format(num1, num2, num1+num2))
    elif botao == 2:
        print('A multiplicação de {} por {} é igual a {}'.format(num1, num2, num1*num2))
    elif botao == 3:
        if num1 > num2:
            print('O maior número é {}'.format(num1))
        elif num1 < num2:
            print('O maior número é {}'.format(num2))
        else:
            print('Os dois números são iguais')
    elif botao == 4:
        print("Digite outros dois números")
        num1 = float(input('número 1: '))
        num2 = float(input('número 2: '))
    elif botao == 5:
        print('FIM')
    else:
        print('Digite uma opção válida!')
