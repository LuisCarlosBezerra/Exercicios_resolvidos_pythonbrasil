"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos
do vetor.
"""
vetor = []
quadrados = 0
for i in range(10):
    while True:
        try:
            numero = int(input('Digite um número inteiro: '))
            if numero >= 0:
                vetor.append(numero)
                break
            else:
                print('Você digitou um valor inválido, tente novamente.')
        except ValueError:
            print('Você digitou um valor inválido, tente novamente.')

    quadrados += (numero * numero)

print(f'\nA soma dos quadrados dos elementos é igual a: {quadrados}')
