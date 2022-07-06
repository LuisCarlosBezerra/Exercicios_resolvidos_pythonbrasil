"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão
é sempre pelo mais barato.
"""
teste = False
while teste is False:
    try:
        produto1 = float(input('Digite o valor do primeiro produto: '))
        produto2 = float(input('Digite o valor do segundo produto: '))
        produto3 = float(input('Digite o valor do terceiro produto: '))
        if (produto1 < 0) or (produto2 < 0) or (produto3 < 0):
            print("Você digitou um produto com preço negativo. Tente novamente.")
        else:
            teste = True
    except ValueError:
        print("Você digitou um valor inválido! Tente novamente.")

contador = 0

if produto1 != produto2 or produto2 != produto3:
    # bloco maior
    if produto1 <= produto2 and produto1 <= produto3:
        contador += 1
        if produto1 != produto2 and produto1 != produto3:
            print(f'Você deverá comprar o produto 1, pois é o mais barato: {"%.2f" % produto1} RS.')

    if produto2 <= produto1 and produto2 <= produto3:
        contador += 1
        if produto2 != produto1 and produto2 != produto3:
            print(f'Você deverá comprar o produto 2, pois é o mais barato: {"%.2f" % produto2} RS.')

    if produto3 <= produto1 and produto3 <= produto2:
        contador += 1
        if produto3 != produto2 and produto1 != produto3:
            print(f'Você deverá comprar o produto 3, pois é o mais barato: {"%.2f" % produto3} RS.')

    if contador == 2:
        if produto1 == produto2:
            print(
                f'Você pode comprar os produtos 1 ou 2, pois tem o mesmo preço e são mais baratos! {"%.2f" % produto1} '
                f'RS')
        if produto2 == produto3:
            print(
                f'Você pode comprar os produtos 2 ou 3, pois tem o mesmo preço e são mais baratos! {"%.2f" % produto2} '
                f'RS')
        if produto1 == produto3:
            print(
                f'Você pode comprar os produtos 1 ou 3, pois tem o mesmo preço e são mais baratos! {"%.2f" % produto1} '
                f'RS')
else:
    print(f'Os preços são todos iguais!')
