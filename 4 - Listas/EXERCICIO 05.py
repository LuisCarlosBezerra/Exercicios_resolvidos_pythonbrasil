"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os
números IMPARES no vetor impar. Imprima os três vetores.
"""
lista_numeros = []
pares = []
impares = []
print('Vamos entrar com 20 números, ok')
for _ in range(20):
    while True:
        try:
            numero = int(input('Digite um número inteiro: '))

            if (numero >= 0) or (numero <= 0):
                lista_numeros.append(numero)
                break
            else:
                print('Você digitou um valor inválido, tente novamente.')

        except ValueError:
            print('Você digitou um valor inválido, tente novamente.')

    numero_str = divmod(numero, 2)
    if numero_str[1] == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'\nPara a lista de valores digitados({lista_numeros}), temos: ')
print(f'PARES: {pares}')
print(f'PARES: {impares}')
