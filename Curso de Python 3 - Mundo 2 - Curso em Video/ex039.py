"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai
se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""
from datetime import date
anoNascimento = int(input('Informe o ano do seu nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

if idade < 18:
    print(f'\nVoçê tem {idade} anos e deve se alistar em {18 - idade} anos!!')
elif idade == 18:
    print(f'\nVoçê já tem {idade} anos e deve se alistar este ano!!')
else:
    print(f'\nVoçê já tem {idade} anos e já passou {idade - 18} anos do prazo do seu alistamento!!')
