"""Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo:  5! = 5 x 4 x 3 x 2 x 1 = 120"""
numero = int(input('Informe um número: '))
fat = numero - 1
total = numero * fat

while fat != 1:
    fat += -1
    total = total * fat
print(f'\nA fatorial de {numero}! = {total}')
