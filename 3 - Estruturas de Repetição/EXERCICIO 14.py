"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de
números impares.
"""
pares = 0
impares = 0

for x in range(1, 11, 1):
    numero = int(input('Digite 10 numeros inteiros: '))
    numero_str = divmod(numero, 2)
    if numero_str[1] == 0:
        print('Número PAR!')
        pares = pares + 1
    else:
        print('Número IMPAR!')
        impares = impares + 1

print(f'Total de números PARES: {pares}\nTotal de números ÍMPARES: {impares}')
