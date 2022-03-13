"""Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores"""
contador = media = maior = menor = 0
resposta = 'S'

while resposta in 'Ss':
    numero = int(input('Informe um número: '))
    media += numero
    contador += 1
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    resposta = input('Deseja continuar [S/N]: ').strip().upper()[0]
print(f'\nA média dos {contador} valores é {media/contador:.2f}!!')
print(f'o menor valor é {menor} e o maior valor é {maior}!!')
