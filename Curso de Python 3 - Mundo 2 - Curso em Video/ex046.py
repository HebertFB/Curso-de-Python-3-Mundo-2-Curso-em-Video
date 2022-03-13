"""Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de
artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles"""
from time import sleep

for c in range(10, 0, -1):
    print(c, "\U0001F4A3")
    sleep(0.5)
print("\U0001F386")
