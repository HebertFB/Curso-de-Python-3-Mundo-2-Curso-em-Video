"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA """
frase = input('Informe a frase: ').upper().split()
fraseJunta = ''.join(frase)
polindromo = ''
for inverso in range(len(fraseJunta)-1, -1, -1):
    polindromo += fraseJunta[inverso]

if fraseJunta == polindromo:
    print(f'\nEstá frase é um polindromo!!')
else:
    print(f'\nEstá frase NÂO é um polindromo!!')
print(f'\nO inverso de {fraseJunta} é {polindromo}')
