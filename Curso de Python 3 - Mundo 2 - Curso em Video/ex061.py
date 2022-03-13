"""Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while """
primeiroTermo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))

ultimoTermo = primeiroTermo+(razao*10)
while primeiroTermo < ultimoTermo:
    print(f'{primeiroTermo}', end=' > ')
    primeiroTermo += razao
print('FIM')
