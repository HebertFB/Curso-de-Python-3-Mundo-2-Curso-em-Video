""" Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos"""
menorPeso = 0
maiorPeso = 0

for pessoas in range(1, 6):
    peso = float(input(f'Informe o peso da {pessoas}ª pessoa: '))
    if pessoas == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print(f'\nO menor peso é de {menorPeso}KG e o maior peso é de {maiorPeso}KG!!')
