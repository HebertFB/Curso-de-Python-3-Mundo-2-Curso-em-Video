"""Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for"""
tabuada = int(input('Informe o número da tabuada desejada: '))

for c in range(1,11):
    print(f'{tabuada} X {c} = {tabuada*c}')
