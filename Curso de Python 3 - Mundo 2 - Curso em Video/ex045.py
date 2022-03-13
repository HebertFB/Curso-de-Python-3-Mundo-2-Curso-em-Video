"""Crie um programa que faça o computador jogar Jokenpô com você."""
from random import randint
from time import sleep

opcoes = ('Pedra', 'Papel', 'Tesoura')
jogadorPC = randint(0, 2)
jogador = input('''\nEscolha uma opção para jogar Jokenpô:
Pedra
Papel
Tesoura
\nOpção: ''').upper()
print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!\n')
sleep(1)

if jogador == 'PEDRA':
    if opcoes[jogadorPC] == 'Tesoura':
        print(f'Voçê jogou {jogador} e a AI jogou {opcoes[jogadorPC]}, voçê Ganhou!!')
    elif opcoes[jogadorPC] == 'Papel':
        print(f'Voçê jogou {jogador} e a AI jogou {opcoes[jogadorPC]}, voçê Perdeu!!')
    elif opcoes[jogadorPC] == 'Pedra':
        print(f'Voçê jogou {jogador} e a AI jogou {opcoes[jogadorPC]}, Empatou!!')
elif jogador == 'PAPEL':
    if opcoes[jogadorPC] == 'Pedra':
        print(f'Voçê jogou {jogador} e a AI jogou {opcoes[jogadorPC]}, voçê Ganhou!!')
    elif opcoes[jogadorPC] == 'Tesoura':
        print(f'Voçê jogou {jogador} e a AI jogou {opcoes[jogadorPC]}, voçê Perdeu!!')
    elif opcoes[jogadorPC] == 'Papel':
        print(f'Voçê jogou {jogador} e a AI jogou {opcoes[jogadorPC]}, Empatou!!')
elif jogador == 'TESOURA':
    if opcoes[jogadorPC] == 'Papel':
        print(f'Voçê jogou {jogador} e a AI jogou {opcoes[jogadorPC]}, voçê Ganhou!!')
    elif opcoes[jogadorPC] == 'Pedra':
        print(f'Voçê jogou {jogador} e a AI jogou {opcoes[jogadorPC]}, voçê Perdeu!!')
    elif opcoes[jogadorPC] == 'Tesoura':
        print(f'Voçê jogou {jogador} e a AI jogou {opcoes[jogadorPC]}, Empatou!!')
else:
    print('Opção Inválida!! Jogue novamente!!')
