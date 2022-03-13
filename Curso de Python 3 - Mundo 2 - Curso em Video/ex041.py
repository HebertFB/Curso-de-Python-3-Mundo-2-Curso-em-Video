""" A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER """

from datetime import date
anoNascimento = int(input('Informe o ano de nascimento do atleta: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

if idade < 10:
    print(f'\nO atleta tem {idade} anos e pertence a categoria MIRIM!!')
elif idade < 15:
    print(f'\nO atleta tem {idade} anos e pertence a categoria INFANTIL!!')
elif idade < 20:
    print(f'\nO atleta tem {idade} anos e pertence a categoria JÚNIOR!!')
elif idade < 26:
    print(f'\nO atleta tem {idade} anos e pertence a categoria SÊNIOR!!')
elif idade > 25:
    print(f'\nO atleta tem {idade} anos e pertence a categoria MASTER!!')
