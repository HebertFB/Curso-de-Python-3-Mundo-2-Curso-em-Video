"""Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de
cada valor serão entregues. OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""
valor = int(input('Quanto voçê quer sacar? R$'))

totalNotas = 0
nota = 50
print('\n')
while True:
    if valor >= nota:
        valor -= nota
        totalNotas += 1
    else:
        print(f'Total de {totalNotas} notas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totalNotas = 0
        if valor == 0:
            break
