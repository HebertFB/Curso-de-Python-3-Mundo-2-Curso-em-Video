"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão"""
primeiroTermo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))

for c in range(primeiroTermo, primeiroTermo+(razao*10), razao):
    print(f'{c}', end=' > ')
print('FIM')
