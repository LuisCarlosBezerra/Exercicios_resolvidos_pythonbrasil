"""
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que
ele mostre os números um ao lado do outro.
"""
contador = 1
lista = []
for _ in range(20):
    print(contador)
    lista.append(contador)
    contador += 1

print()
contador = 1
for _ in range(20):
    print(contador, end=' ')
    contador += 1

print()
print(lista)
