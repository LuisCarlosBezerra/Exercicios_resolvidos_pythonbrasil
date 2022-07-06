"""
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
"""
print('NUMEROS IMPARES ENTRE 0 E 50')

for numero in range(50):
    numero_str = divmod(numero, 2)
    if numero_str[1] != 0:
        print(numero)
