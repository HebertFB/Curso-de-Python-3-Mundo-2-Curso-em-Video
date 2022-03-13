"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""

valorCasa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o seu salario mensal: R$'))
anosAPagar = int(input('Em quantos anos de financiamento: '))

prestacaoMensal = (valorCasa/anosAPagar) / 12

if prestacaoMensal > (salario*0.3):
    print(f'\nEmpréstimo negado!!! '
          f'\nPois a prestação mensal de R${prestacaoMensal:.2f} excedeu 30% do salário de R${salario:.2f} !!')
else:
    print(f'\nEmpréstimo concedido!!! '
          f'\nPois a prestação mensal de R${prestacaoMensal:.2f} é igual ou menor que 30% do salário '
          f'de R${salario:.2f} !!')
