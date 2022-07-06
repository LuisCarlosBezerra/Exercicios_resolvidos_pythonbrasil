"""
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que
ele mostre os números um ao lado do outro.
"""
numero = 1
lista = []
for _ in range(1, 21, 1):
    lista.append(numero)
    print(numero)
    numero += 1

numero = 1
lista = []
print()

for _ in range(1, 21, 1):
    lista.append(numero)
    print(numero, end=' ')
    numero += 1
