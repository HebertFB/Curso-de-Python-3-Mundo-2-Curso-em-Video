"""Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos """
primeiroTermo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
contador = 1
quantosTermos = 10
total = 0

while quantosTermos != 0:
    total += quantosTermos
    while contador <= total:
        print(f'{primeiroTermo}', end=' > ')
        primeiroTermo += razao
        contador += 1
    print("PAUSA")
    quantosTermos = int(input('Deseja mais quantos termos? '))
print(f'\nPA finalizada com {total} termos!!')
