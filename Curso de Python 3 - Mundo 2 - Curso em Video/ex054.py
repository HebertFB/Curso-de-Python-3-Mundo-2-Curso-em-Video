"""Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores"""
from datetime import date
anoAtual = date.today().year
maiorIdade = 0
menorIdade = 0

for pessoas in range(1, 8):
    anoNasc = int(input(f'Informe o ano de nascimento da {pessoas}ª pessoa: '))
    idade = anoAtual - anoNasc
    if idade >= 18:
        maiorIdade += 1
    else:
        menorIdade += 1
print(f'\n{maiorIdade} pessoas já são maiores de idade!!')
print(f'{menorIdade} pessoas ainda são menores de idade!!')
