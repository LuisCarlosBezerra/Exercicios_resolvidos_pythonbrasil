"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""
# SOLUÇÃO 01

lista = []

for _ in range(1, 11, 1):
    while True:
        try:
            numero = float(input('Entre com um valor real: '))
            if (numero >= 0) or (numero <= 0):
                lista.append(numero)
                break
        except ValueError:
            print('Você digitou um valor inválido, tente novamente. ')

lista.reverse()
print(f'Os números, em ordem inversa, são: \n{lista}')
