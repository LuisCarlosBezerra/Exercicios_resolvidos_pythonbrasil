"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""
teste = False
while teste is False:
    try:
        numero1, numero2, numero3 = int(input('Insira um número NATURAL: ')), int(
            input('Insira outro número NATURAL: ')), float(input('Insira um número REAL: '))
        teste = True
    except ValueError:
        print("Digite valores válidos, respeitando o que se pede")

print(f'O produto do dobro do primeiro com metade do segundo: {"%.2f" % ((2 * numero1) * (numero2 / 2))}')
print(f'A soma do triplo do primeiro com o terceiro: {"%.2f" % ((3 * numero1) + numero3)}')
print(f'O terceiro elevado ao cubo: {"%.2f" % (numero3 * numero3 * numero3)}')
