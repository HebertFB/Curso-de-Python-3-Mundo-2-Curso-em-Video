"""Crie um programa que leia a idade e o sexo de várias pessoas.A cada
pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""
maioresIdade = homens = mulheresJovens = 0

while True:
    idade = int(input('\nInforme a idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = input('Informe o sexo [F/M]: ').strip().upper()[0]
    if idade >= 18:
        maioresIdade += 1
    if sexo == 'F' and idade < 20:
        mulheresJovens += 1
    if sexo == 'M':
        homens += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if opcao == 'N':
        break
print(f'\nHá {maioresIdade} maiores de 18 anos\nHá {homens} homens!\nHá {mulheresJovens} mulheres com menos de 20 anos!!')
