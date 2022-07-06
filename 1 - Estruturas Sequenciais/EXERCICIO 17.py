"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam RS 80,00 ou em galões de 3,6 litros, que custam RS 25,00. Informe ao usuário as
quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

comprar apenas latas de 18 litros;

comprar apenas galões de 3,6 litros;

misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde
os valores para cima, isto é, considere latas cheias. """
# TESTANDO A VALIDADE DOS VALORES INSERIDOS
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

# PROCESSAMENTO
LITROS = (areapintada / 6)
LATAS = LITROS / 18
GALOES = LITROS / 3.6

# CALCULANDO AS LATAS
if (LATAS // 1 == LATAS):
    # --> ESTA FUNÇÃO VERIFICA SE O NUMERO É INTEIRO, BASICAMENTE PEGA SOMENTE A PARTE
    # INTEIRA DO NUMERO E COMPARA COM O NUMERO ORIGINAL, ISTO PARA FINS DE SABER SE PASSOU ALGUMA COISA DE UMA LATA
    # INTEIRA, SENDO NECESSÁRIO OU NÃO O ACRÉSCIMO DE UMA LATA, OU GALÃO <--
    custoL = LATAS * 80
else:
    LATAS = (LATAS // 1) + 1
    custoL = LATAS * 80

# CALCULANDO OS GALÕES
if GALOES // 1 == GALOES:
    custoG = GALOES * 25
else:
    GALOES = (GALOES // 1) + 1
    custoG = GALOES * 25

print(
    f'EM LATAS: você comprará {"%.0f" % LATAS} latas, totalizando {"%.2f" % custoL} R$\nEM GALÕES: você comprará '
    f'{"%.0f" % GALOES} galões, totalizando {"%.2f" % custoG} R$')

# CALCULANDO O MELHOR PREÇO
MODULO = divmod(LITROS, 18)
# print(MODULO)
MODULOG = divmod(MODULO[1], 3.6)
# print(MODULOG)
# CUSTO = (80 * MODULO[0]) + (25 * MODULOG[0])

# CASO O NÚMERO A DIVISÃO LATAS NÃO RETORNE RESTO DE LITROS
if MODULO[1] == 0:
    CUSTO = (80 * (MODULO[0] + 1))
    print(
        f'Caso opte por ter um desperdício menor de tinta, comprará {"%.0f" % (MODULO[0] + 1)} LATA(S), pagando o '
        f'total de {"%.2f" % CUSTO} REAIS.')


# CASO HAJA QUANTIA DE RESTO DE LITROS DA DIVISÃO DE LATAS
else:  # CASO O RESTO NÃO ULTRAPASSE 3 GALÕES, POIS O QUARTO IMPLICARIA EM VALOR MAIOR QUE O DE UMA LATA.
    if MODULO[1] <= 10.6:
        if MODULOG[1] > 0:
            CUSTO = (80 * MODULO[0] + (25 * (MODULOG[0] + 1)))
            # GALOES = MODULOG[0] + 1
            print(
                f'Caso opte por ter um disperdício menor de tinta, comprará {"%.0f" % (MODULO[0])} LATA(S) e '
                f'{"%.0f" % (MODULOG[0] + 1)} GALÃO(ÕES), pagando o total de {"%.2f" % CUSTO} REAIS.')

        else:
            CUSTO = (80 * MODULO[0] + (25 * MODULOG[0]))
            print(
                f'Caso opte por ter um disperdício menor de tinta, comprará {"%.0f" % (MODULO[0])} LATA(S) e '
                f'{"%.0f" % (MODULOG[0])} GALÃO(ÕES), pagando o total de {"%.2f" % CUSTO} REAIS.')

    else:  # VALOR MAIOR QUE 10.6 LITROS, EM GALÕES ULTRAPASSARIA O VALOR DA LATA.
        CUSTO = (80 * (MODULO[0] + 1))
        print(
            f'Caso opte por ter um desperdício menor de tinta, comprará {"%.0f" % (MODULO[0] + 1)} LATA(S), pagando o '
            f'total de {"%.2f" % CUSTO} REAIS.')
