"""Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre elas (desconsiderando o flag)"""
soma = contador = 0
while True:
    numero = int(input('Informe um número [999 p/ parar]: '))
    if numero == 999:
        break
    contador += 1
    soma += numero
print(f'\nForam digitados {contador} números e a soma entre eles é {soma}!!')
