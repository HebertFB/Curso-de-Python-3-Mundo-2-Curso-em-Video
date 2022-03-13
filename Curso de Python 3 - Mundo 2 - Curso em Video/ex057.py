"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto """
sexo = input('Informe o sexo da pessoa [M/F]: ').strip().upper()[0]
while sexo not in 'FfMm':
    sexo = input('Dados inválidos. Por favor, informe o sexo da pessoa [M/F]: ').strip().upper()[0]
print(f'\nSexo {sexo} registrado com sucesso!!')
