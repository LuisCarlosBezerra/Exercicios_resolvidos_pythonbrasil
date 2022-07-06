"""
Faça um Programa que peça dois números e imprima o maior deles.
"""
teste = False
while teste is False:
    try:
        numero1 = float(input('Insira o primeiro número: '))
        numero2 = float(input('Insira o segundo número: '))
        teste = True
    except ValueError:
        print("Digite um valor válido!")

if numero1 != numero2:
    if numero1 > numero2:
        print(f'O número maior é {numero1}')
    if numero1 < numero2:
        print(f'O número maior é {numero2}')

else:
    print(f'Os números são iguais!')
