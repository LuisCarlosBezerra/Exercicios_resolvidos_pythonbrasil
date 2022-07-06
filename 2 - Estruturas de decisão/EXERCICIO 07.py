"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
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

maior, menor = 0, 0
if numero1 != numero2 or numero2 != numero3:
    # bloco maior
    if numero1 >= numero2 and numero1 >= numero3:
        maior = numero1
    if numero2 >= numero1 and numero2 >= numero3:
        maior = numero2
    if numero3 >= numero1 and numero3 >= numero2:
        maior = numero3

    # bloco menor
    if numero1 <= numero2 and numero1 <= numero3:
        menor = numero1
    if numero2 <= numero1 and numero2 <= numero3:
        menor = numero2
    if numero3 <= numero1 and numero3 <= numero2:
        menor = numero3

    print(f'O MAIOR deles é o: {maior}\nO MENOR deles é o: {menor}')
else:
    print(f'Os números são iguais!')
