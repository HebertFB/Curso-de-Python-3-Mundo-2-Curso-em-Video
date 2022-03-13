"""Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais"""

numeroUm = int(input('Informe o primeiro número: '))
numeroDois = int(input('Informe o segundo número: '))

if numeroUm > numeroDois:
    print(f'\nO número {numeroUm} é maior que o segundo número!!')
elif numeroDois > numeroUm:
    print(f'\nO número {numeroDois} é maior que o primeiro número!!')
else:
    print(f'\nNão existe valor maior, os dois são iguais!!')
