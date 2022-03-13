"""Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes"""

lado1 = float(input('Informe o primeiro lado: '))
lado2 = float(input('Informe o segundo lado: '))
lado3 = float(input('Informe o terceiro lado: '))

if lado1 == lado2 == lado3 == lado1:
    print('\nTodos os lados são iguais! Que formar um triângulo equilátero!')
elif lado1 == lado2 and lado1 != lado3 or lado1 == lado3 and lado1 != lado2 or lado2 == lado3 and lado2 != lado1:
    print('\nHá dois lados iguais e um diferente! Que formar um triângulo isósceles!')
elif lado1 != lado2 != lado3 != lado2:
    print('\nTodos os lados são diferentes! Que formar um triângulo escaleno!')
else:
    print('\nOs lados informados NÃO podem formar um triângulo!')
