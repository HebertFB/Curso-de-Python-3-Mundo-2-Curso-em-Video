"""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
que forem pares. Se o valor digitado for ímpar, desconsidere-o"""
soma = 0
pares = 0
for c in range(0, 6):
    numero = int(input(f'Informe o número {c+1}: '))
    if numero % 2 == 0:
        soma += numero
        pares += 1
print(f'\nA soma dos {pares} pares informados é: {soma}')
