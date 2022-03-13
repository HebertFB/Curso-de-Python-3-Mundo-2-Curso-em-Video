"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida"""

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f'\nSeu IMC é {imc:.2f}! Voçê está abaixo do Peso!!!')
elif imc < 25:
    print(f'\nSeu IMC é {imc:.2f}! Voçê está com o Peso Ideal!!!')
elif imc < 30:
    print(f'\nSeu IMC é {imc:.2f}! Voçê está com Sobrepeso!!!')
elif imc < 40:
    print(f'\nSeu IMC é {imc:.2f}! Voçê está com Obesidade!!!')
else:
    print(f'\nSeu IMC é {imc:.2f}! Voçê está com Obesidade Mórbida!!!')
