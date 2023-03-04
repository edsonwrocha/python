print('==+=='*11)
titulo = str('Simule o financiamento da sua casa dos {}sonhos!!!{}'.format('\033[34m', '\033[m'))
print(titulo.center(60))
print('==+=='*11)
valor_casa = float(input('\nDigite o valor da casa que deseja financiar: '))
salario = float(input('Digite o seu salário atual: '))
tmp_financiamento = float(input('Digite em quantos anos você quer dividir a casa: '))
if tmp_financiamento != 0:
    mensalidade = valor_casa / (tmp_financiamento * 12)

if tmp_financiamento == 0:
    print('\033[2;31mERRO!\033[m Você digitou 0 anos na segunda opção, tente outro valor')
elif tmp_financiamento % 2 > 0 and tmp_financiamento % 2 < 1:
    print('\033[2;31mERRO!\033[m É necessário que o tempo seja preenchido em anos inteiros, tente novamente!')
elif valor_casa == 0:
    print('\033[2;31mERRO!\033[m O valor da casa precisa ser maior do quê R$0, tente novamente!')
elif mensalidade > (30/100)*salario:
    print('\033[2;31mEmpréstimo NEGADO!\033[m O valor da mensalidade excede 30% do seu salário')
else:
    print('\033[2;32mEmprestimo APROVADO!\033[m Sua mensalidade para o pagamento em {} anos ficou R${:.2f}'.format(int(tmp_financiamento), mensalidade))
