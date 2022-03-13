"""Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)"""
soma = 0
contador = 0
numero = 0

while numero != 999:
    numero = int(input('Informe o valor [999 p/ sair]: '))
    if numero != 999:
        soma += numero
        contador += 1
print(f'\nA soma dos {contador} digitos informados é de {soma}!!')
