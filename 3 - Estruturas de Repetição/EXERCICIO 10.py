"""
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido
por eles.
"""
inicio = int(input('Digite o valor inicial do intervalo: '))
fim = int(input('Digite o valor final do intervalo: '))

for _ in range(inicio, fim + 1, 1):
    print(_)
