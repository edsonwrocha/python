preco = float(input('Digite o valor do produto: '))
print("""Formas de pagamento:
1- À vista dinheiro/cheque: 10% desconto
2 -À vista cartão: 5% desconto
3 -2x no cartão sem juros
4 -3x ou mais vezes no cartão: 20% de juros""")
pagamento = int(input('Digite a forma de pagamento: '))

if pagamento == 1:
    desconto = preco * (90/100)
    print('O seu produto custará R${}'.format(desconto))
elif pagamento == 2:
    desconto = preco * (95/100)
    print('O seu produto custará R${}'.format(desconto))
elif pagamento == 3:
    mensalidade = preco / 2
    print('O seu produto será pago em 2x de R${}'.format(mensalidade))
elif pagamento >= 4:
    parcelas = int(input('Digite o número de parcelas: '))
    if parcelas == 0:
        print('ERRO, valor das parcelas deve ser diferente de 0')
    else:
        mensalidade = (preco / parcelas) * (120/100)
        print('O seu produto será pago em {}x de R${}'.format(parcelas, mensalidade))
