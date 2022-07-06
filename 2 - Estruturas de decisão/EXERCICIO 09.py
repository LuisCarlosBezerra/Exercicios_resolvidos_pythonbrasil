"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
teste = False
while teste is False:
    try:
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))
        numero3 = float(input('Digite o terceiro número: '))
        teste = True
    except ValueError:
        print('Você digitou um valor inválido! Tente novamente.')

maior, menor, meio = 0, 0, 0

# maior
if numero1 >= numero2 and numero1 >= numero3:
    maior = numero1
if numero2 >= numero3 and numero2 >= numero1:
    maior = numero2
if numero3 >= numero2 and numero3 >= numero1:
    maior = numero3

# menor
if numero1 <= numero2 and numero1 <= numero3:
    menor = numero1
if numero2 <= numero3 and numero2 <= numero1:
    menor = numero2
if numero3 <= numero2 and numero3 <= numero1:
    menor = numero3

# meio
if (numero2 <= numero1 <= numero3) or (numero3 <= numero1 <= numero2):
    meio = numero1
if (numero3 <= numero2 <= numero1) or (numero1 <= numero2 <= numero3):
    meio = numero2
if (numero2 <= numero3 <= numero1) or (numero2 >= numero3 >= numero1):
    meio = numero3

print('Os números em ordem DECRESCENTE são: ')
print(f'{maior}\n{meio}\n{menor}')
