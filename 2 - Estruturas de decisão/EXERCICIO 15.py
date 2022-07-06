"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""
while True:
    try:
        lado1, lado2, lado3 = float(input('Digite o PRIMEIRO lado do triângulo: ')), float(
            input('Digite o SEGUNDO lado do triângulo: ')), float(input('Digite o TERCEIRO lado do triângulo: '))
        if (lado1 > 0) and (lado2 > 0) and (lado3 > 0):
            break
        else:
            print('Você digitou um valor negativo! Digite valores positivos.')
    except ValueError:
        print("Valor digitado é inválido! Tente novamente.")

equilatero = False

if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:

    if lado1 == lado2 and lado2 == lado3:
        print('O triângulo é EQUILÁTERO!')
        equilatero = True

    if lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        print('O triângulo é ESCALENO!')

    if equilatero is False and (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
        print('O triângulo é ISÓSCELES!')

else:
    print('Os lados inseridos NÃO FORMAM um triângulo!')

