"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo"""
while True:
    print('------ TABUADA ------')
    numero = int(input('Informe o número: '))
    if numero < 0:
        break
    print('-' * 21)
    for c in range(1, 11):
        print(f'{numero} X {c} = {numero*c}')
print(f'\nO número {numero} é negativo!!')
