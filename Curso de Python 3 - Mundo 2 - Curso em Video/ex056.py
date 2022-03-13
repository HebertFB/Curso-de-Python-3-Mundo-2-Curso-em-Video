"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do
homem mais velho e quantas mulheres têm menos de 20 anos"""
mediaIdade = 0
homemVelho = ''
idadeVelho = 0
mulheresJovens = 0

for pessoas in range(1, 5):
    nome = input(f'------- {pessoas}ª Pessoa -------'
                 f'\nNome: ').strip()
    idade = int(input(f'Idade: '))
    sexo = input(f'Sexo [M/F]: ').strip().upper()
    mediaIdade += idade
    if sexo == 'M':
        idadeVelho = idade
        homemVelho = nome
        if idade > idadeVelho:
            homemVelho = nome
    if sexo == 'F' and idade < 20:
        mulheresJovens += 1
print(f'\nA média de idade do grupo é de {mediaIdade/4} anos!!')
print(f'O homem mais velho é {homemVelho}!!')
print(f'E {mulheresJovens} mulher tem menos de 20 anos!!')
