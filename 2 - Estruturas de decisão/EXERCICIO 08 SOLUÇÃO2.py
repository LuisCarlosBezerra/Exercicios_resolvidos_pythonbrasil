"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão
é sempre pelo mais barato.
"""
teste = False
while teste is False:
    try:
        produto1 = float(input("Digite o preço do primeiro produto: "))
        produto2 = float(input("Digite o preço do segundo produto: "))
        produto3 = float(input("Digite o preço do terceiro produto: "))
        if (produto1 < 0) or (produto2 < 0) or (produto3 < 0):
            print("Você digitou um preço negativo! Tente novamente.")
        else:
            teste = True
    except ValueError:
        print("Você digitou um valor inválido! Tente novamente.")

if produto1 != produto2 or produto1 != produto3:

    # PRODUTO1
    if (produto1 < produto2) and (produto1 < produto3):
        print(f'Você deverá comprar o produto 1, pois tem o melhor preço: {"%.2f" % produto1} R$')
    if produto1 == produto2:
        print(f'Você deverá comprar os produtos 1 e 2, pois tem o melhor preço: {"%.2f" % produto1} R$')
    if produto1 == produto3:
        print(f'Você deverá comprar os produtos 1 e 3, pois tem o melhor preço: {"%.2f" % produto1} R$')

    # PRODUTO2
    if (produto2 < produto1) and (produto2 < produto3):
        print(f'Você deverá comprar o produto 2, pois tem o melhor preço: {"%.2f" % produto2} R$')
    if produto2 == produto3:
        print(f'Você deverá comprar os produtos 2 e 3, pois tem o melhor preço {"%.2f" % produto2} R$')

    # PRODUTO3
    if (produto3 < produto1) and (produto3 < produto2):
        print(f'Você deverá comprar o produto 3, pois tem o melhor preço: {"%.2f" % produto3} R$')


else:
    print("Os preços digitados são iguais para os 3 produtos!")
