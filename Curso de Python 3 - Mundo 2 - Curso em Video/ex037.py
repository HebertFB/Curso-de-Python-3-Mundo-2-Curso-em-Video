"""Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""

numero = int(input('Informe um número inteiro: '))
opcao = int(input('Conversão - Escolha '
                  '\n1 para binário'
                  '\n2 para octal'
                  '\n3 para hexadecimal'
                  '\nOpção: '))

if opcao == 1:
    print(f'\n{numero} convertido para binario é {bin(numero)[2:]}')
elif opcao == 2:
    print(f'\n{numero} convertido para octal é {oct(numero)[2:]}')
elif opcao == 3:
    print(f'\n{numero} convertido para hexadecimal é {hex(numero)[2:]}')
else:
    print('Opção inválida!!')
