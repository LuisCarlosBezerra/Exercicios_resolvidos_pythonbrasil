"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""
# SOLUÇÃO 02

lista = []

for _ in range(1, 5, 1):
    while True:
        try:
            numero = float(input('Digite um numero real: '))
            if (numero >= 0) or (numero <= 0):
                lista.append(numero)
                break
            else:
                print('Valor inválido digitado, tente novamente.')
        except ValueError:
            print('Você digitou um valor inválido, tente novamente.')

contador_reverso = -1
for i in range(4):
    print(lista[contador_reverso], end=" ")
    contador_reverso -= 1
