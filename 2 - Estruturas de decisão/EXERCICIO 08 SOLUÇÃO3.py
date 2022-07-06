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
        if (produto1 > 0) and (produto2 > 0) and (produto3 > 0):
            teste = True
        else:
            print('Você digitou um preço negativo! Tente novamente.')
    except ValueError:
        print('Você digitou um valor inválido! Tente novamente.')

# lista de produtos que ordenará e retornará o mais barato
lista_de_produtos = [produto1, produto2, produto3]
lista_de_produtos.sort()

# Dicionário para chamar o nome do produto mais barato
dic_prod = {produto1: 'produto 1', produto2: 'produto 2', produto3: 'produto 3'}

# print(dic_prod.get(lista_de_produtos[0]))


print(
    f'O produto mais barato é o {dic_prod.get(lista_de_produtos[0])}, que tem o valor de '
    f'{"%.2f" % lista_de_produtos[0]} R$')
