"""Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer"""
from random import randint
print('Tente advinha! Pensando em um número entre 0 a 10...\n')
pc = randint(0, 10)
acertou = False
tentativas = 0

while not acertou:
    player = int(input('Qual número o computador pensou? '))
    tentativas += 1
    if player == pc:
        acertou = True
    else:
        if player < pc:
            print('Errou! é MAIS! Tente Novamente!!')
        elif player > pc:
            print('Errou! é MENOS! Tente Novamente!!')
print(f'\nVocê acertou na {tentativas} tentativa! O número é {pc}')
