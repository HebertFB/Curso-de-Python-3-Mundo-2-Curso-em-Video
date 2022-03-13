"""Faça um programa que jogue par ou ímpar com o computador.O jogo só será interrompido quando
o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo"""
from random import randint
totalVitorias = 0

while True:
    pc = randint(0, 11)
    numero = int(input('Informe um número: '))
    soma = pc + numero
    opcao = ' '
    while opcao not in 'PI':
        opcao = input('Escolhar: Ímpar ou Par [I/P]? ').strip().upper()[0]
    print(f'O computador jogou {pc} e voçê jogou {numero}, total de {soma} ', end='')
    print('deu PAR!!' if soma % 2 == 0 else 'deu ÍMPAR!!')
    if opcao == 'P':
        if soma % 2 == 0:
            totalVitorias += 1
            print(f'Voçê GANHOU!!')
        else:
            print(f'Voçê PERDEU!!')
            break
    elif opcao == 'I':
        if soma % 2 == 1:
            totalVitorias += 1
            print(f'Voçê GANHOU!!')
        else:
            print(f'Voçê PERDEU!!')
            break
    print('Vamos jogar novamente...\n')
print(f'\nVoçê ganhou {totalVitorias} vezes consecutivas!!')
