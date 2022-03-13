"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""
totalCompra = produtosCaros = maisBarato = contador = 0
nomeBarato = ' '

while True:
    produto = input('Informe o nome do produto: ')
    preco = float(input('Informe o valor: R$ '))
    totalCompra += preco
    contador += 1
    if preco > 1000:
        produtosCaros += 1
    if contador == 1 or preco < maisBarato:
        maisBarato = preco
        nomeBarato = produto
    opcao = ' '
    while opcao not in 'SN':
        opcao = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if opcao == 'N':
        break
print(f'\nTotal da compra: R${totalCompra:.2f}')
print(f'Há {produtosCaros} produtos que custa mais de R$1000.00!!')
print(f'O produto mais barato é {nomeBarato} que custa R${maisBarato:.2f}!!')
