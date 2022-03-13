"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo """
numero = int(input('Informe um número: '))
total = 0
for c in range(1, numero+1):
    if numero % c == 0:
        total += 1
if total == 2:
    print(f'\nO número {numero} é primo!!')
else:
    print(f'\nO número {numero} não é primo!!')
