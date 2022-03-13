"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros"""

valorProduto = float(input('Insira o valor do produto: R$'))
opcao = int(input('''\nDigite a opção de pagamento
1 - à vista dinheiro/cheque
2 - à vista no cartão
3 - em até 2x no cartão
4 - 3x ou mais no cartão
Opção: '''))

if opcao == 1:
    print(f'\nOpção 1 escolhida\nValor a ser pago com 10% de desconto será de R${valorProduto-(valorProduto*0.1):.2f}!')
elif opcao == 2:
    print(f'\nOpção 2 escolhida\nValor a ser pago com 5% de desconto será de R${valorProduto-(valorProduto*0.05):.2f}!')
elif opcao == 3:
    print(f'\nOpção 3 escolhida\n\nSua compra será parcelada em 2x de R${(valorProduto/2):.2f}'
          f'\nValor total a ser pago será de R${(valorProduto):.2f}!')
elif opcao == 4:
    parcelas = int(input(f'\nOpção 4 escolhida\nQuantas parcelas? '))
    print(f'\nSua compra será parcelada em {parcelas}x de R${(valorProduto + (valorProduto * 0.2))/parcelas:.2f}')
    print(f'\nValor a ser pago no total com 20% de juros será de R${valorProduto+(valorProduto*0.2):.2f}!')
else:
    print('Opção Inválida!!!')
