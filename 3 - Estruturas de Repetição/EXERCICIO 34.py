"""
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele
que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele
é ou não um número primo.
"""
numero = int(input('Digite um número para saber se é primo: '))
acumulador_divisores = 0

for i in range(1, numero + 1, 1):
    numero_str = divmod(numero, i)
    if numero_str[1] == 0:
        acumulador_divisores += 1

    if acumulador_divisores > 2:
        break

# print(f'{acumulador_divisores}')
if acumulador_divisores == 2:
    print('É PRIMO')

else:
    print('NÃO É PRIMO')
