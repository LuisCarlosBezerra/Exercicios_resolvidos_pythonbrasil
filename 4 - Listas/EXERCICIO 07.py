"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""
lista_numeros = []
multiplicar = 1

for i in range(5):
    while True:
        try:
            numero = float(input('Entre com um número natural: '))
            if numero >= 0:

                break
            else:
                print('Você digitou um valor inválido. Digite um numero natural.')
        except ValueError:
            print('Valor inválido digitado! Tente novamente.')

    multiplicar *= numero
    lista_numeros.append(numero)

print(f'\nOs números digitados foram: {lista_numeros}')
print(f'A soma destes números é igual a: {sum(lista_numeros)}')
print(f'O produto de todos os números é: {multiplicar}')
