"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
preço total. """
# TESTANDO A VALIDADE DA ENTRADA, SE SÃO NÚMEROS E VÁLIDOS
print('LOJA DE TINTAS TINTEIRO BOM')
teste = False
while teste is False:
    try:
        areapintada = float(input('Digite a área total a ser pintada (m2) '))
        if areapintada <= 0:
            print("Você digitou um valor nulo ou negativo. Tente novamente.")
        else:
            teste = True
    except ValueError:
        print("Você digitou um valor inválido. Tente novamente.")

# PROCESSAMENTO E SAÍDA DE DADOS
latas = (areapintada / 3) / 18

if latas // 1 == latas:
    custo = latas * 80
    if latas == 1:
        print(
            f'Para esta área a ser pintada, você deve comprar {"%.0f" % latas} lata, que custará {"%.2f" % custo} '
            f'reais.')
    else:
        print(
            f'Para esta área a ser pintada, você deve comprar {"%.0f" % latas} lata(s), que custarão {"%.2f" % custo} '
            f'reais.')

else:
    latas = (latas // 1) + 1
    custo = latas * 80
    if latas == 1:
        print(
            f'Para esta área a ser pintada, você deve comprar {"%.0f" % latas} lata, que custará {"%.2f" % custo} '
            f'reais.')
    else:
        print(
            f'Para esta área a ser pintada, você deve comprar {"%.0f" % latas} lata(s), que custarão {"%.2f" % custo} '
            f'reais.')
