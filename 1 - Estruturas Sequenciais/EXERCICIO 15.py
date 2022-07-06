"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre
o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o
salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:
(+) Salário Bruto : R$
(-) IR (11%) : R$
(-) INSS (8%) : R$
(-) Sindicato ( 5%) : R$
(=) Salário Liquido : R$
"""
# TESTANDO SE AS VARIÁVEIS SÃO NÚMEROS E POSITIVOS
teste = False
while teste is False:
    try:
        horas, valorhora = float(input('Digite as horas trabalhadas no mês: ')), float(
            input('Digite o valor de uma hora trabalhada: '))
        if (horas < 0) or (valorhora < 0):
            print("Você digitou um valor negativo. Tente novamente.")
        else:
            teste = True
    except ValueError:
        print("Você digitou um valor inválido. Tente novamente.")

# PROCESSAMENTO E SAÍDA DE DADOS
salariobruto = horas * valorhora
IR = salariobruto * 0.11
INSS = salariobruto * 0.08
SINDICATO = salariobruto * 0.05
liquido = salariobruto - SINDICATO - INSS - IR

print(
    f'\nO seu SALÁRIO BRUTO é igual a: {"%.2f" % salariobruto} R$.\n\nOS SEUS DESCONTOS SÃO:\nImposto de renda: {"%.2f" % IR} R$.\nINSS: {"%.2f" % INSS} R$.\nSindicato: {"%.2f" % SINDICATO} R$.\n\nO seu salário LIQUIDO (retirado os descontos), é de {"%.2f" % liquido} R$.')
