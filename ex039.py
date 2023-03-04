from datetime import date
nascimento = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - nascimento

if idade > 18:
    print('Você não precisa se alistar')
    prazo = idade - 18
    print('Já passaram {} ano(s) do seu prazo'.format(prazo))
elif idade < 18:
    print('Você precisa se alistar no serviço militar')
    prazo = 18 - idade
    print('Faltam {} ano(s) para você se alistar!'.format(prazo))
else:
    print('Esse é o ano do seu alistamento')
    print('Procure uma junta ou entre no site: \033[4;35mwww.alistamentomilitar.org\033[37m')
