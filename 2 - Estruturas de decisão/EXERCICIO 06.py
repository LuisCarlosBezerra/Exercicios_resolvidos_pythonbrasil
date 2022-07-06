"""
Faça um Programa que leia três números e mostre o maior deles.
"""
teste = False
while teste is False:
    try:
        numero1 = float(input('Insira o primeiro número: '))
        numero2 = float(input('Insira o segundo número: '))
        numero3 = float(input('Insira o terceiro número '))
        teste = True
    except ValueError:
        print("Você digitou um valor inválido! Tente novamente.")

if numero1 != numero2 or numero2 != numero3:
    if numero1 > numero2 and numero1 > numero3:
        print(f'O número maior é {numero1}')
    if numero2 > numero1 and numero2 > numero3:
        print(f'O número maior é {numero2}')
    if numero3 > numero1 and numero3 > numero2:
        print(f'O número maior é {numero3}')

else:
    print(f'Os números são iguais!')
