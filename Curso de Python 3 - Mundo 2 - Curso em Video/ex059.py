"""Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso"""
numeroUm = int(input('Informe o primeiro valor: '))
numeroDois = int(input('Informe o segundo valor: '))
opcao = 0

while opcao != 5:
    print('''\n-------- MENU --------
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
----------------------''')
    opcao = int(input('Informe a opção desejada: '))

    if opcao == 1:
        print(f'\nA soma de {numeroUm} + {numeroDois} é {numeroUm + numeroDois}!!')
    elif opcao == 2:
        print(f'\nA multiplicação de {numeroUm} X {numeroDois} é {numeroUm * numeroDois}!!')
    elif opcao == 3:
        if numeroUm > numeroDois:
            print(f'\nO primeiro valor "{numeroUm}" é maior que o segundo valor "{numeroDois}"!!')
        elif numeroUm < numeroDois:
            print(f'\nO segundo valor "{numeroDois}" é maior que o primeiro valor "{numeroUm}"!!')
    elif opcao == 4:
        numeroUm = int(input('\nInforme novamente o primeiro valor: '))
        numeroDois = int(input('Informe novamente o segundo valor: '))
    elif opcao == 5:
        print('Saindo do programa...')
    else:
        print('Opção Inválida!! Tente Novamente!!')
