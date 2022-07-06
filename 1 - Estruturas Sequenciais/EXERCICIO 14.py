"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu
trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São
Paulo (50 quilos), deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que
leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do
limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens
adequadas. """
excesso = 0

# FILTRANDO VALORES FLOAT
teste = False
while teste is False:
    try:
        pesopeixe = float(input('Insira o peso de peixes pescados: '))
    except ValueError:
        print("Você digitou um valor inválido! Tente novamente.")

    # FILTRANDO SOMENTE VALORES POSITIVOS
    if pesopeixe < 0:
        print("Você digitou um valor inválido.Tente novamente.")
    else:
        teste = True

# PROCESSAMENTO DE INFORMAÇÕES E SAÍDA
if pesopeixe > 50:
    excesso = (pesopeixe - 50)
    multa = excesso * 4
    print(
        f'Peso total de peixes: {"%.2f" % pesopeixe} quilos; Valor excedente: {"%.2f" % excesso} quilo(s); Multa a '
        f'ser paga: {"%.2f" % multa} R$.')

else:
    multa = 0
    print(
        f'Peso total de peixes: {"%.2f" % pesopeixe} quilos. Valor menor ou igual a 50 quilos não implica em excesso '
        f'e multa!')
