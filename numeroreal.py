# Crie um programa que leia um numero real qualquer pelo teclado e mostra na tela a sua porçao inteira
import math
numero = float(input('Digite um numero qualquer'))
print('o numero inteiro de {} e = a {} '.format(numero, math.floor(numero)))
