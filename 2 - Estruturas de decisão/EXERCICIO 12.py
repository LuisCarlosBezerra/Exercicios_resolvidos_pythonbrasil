"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:

Salário Bruto até 900 (inclusive) - isento

Salário Bruto até 1500 (inclusive) - desconto de 5%

Salário Bruto até 2500 (inclusive) - desconto de 10%

Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""
teste = False
while teste is False:
    try:
        horas_trabalhadas = float(input('Digite quantas horas trabalhadas no mês: '))
        valor_hora = float(input('Digite o valor de cada hora trabalhada: '))
        if valor_hora > 0 and horas_trabalhadas > 0:
            teste = True
        else:
            print('Você digitou um valor negativo! Tente novamente.')
    except ValueError:
        print('Você digitou um valor inválido, tente novamente.')

salario = horas_trabalhadas * valor_hora
if 0 < salario <= 900:
    imposto_renda = 0
    desconto = 0
if 900 < salario <= 1500:
    imposto_renda = salario * 0.05
    desconto = 5
if 1500 < salario <= 2500:
    imposto_renda = salario * 0.1
    desconto = 10
if salario > 2500:
    imposto_renda = salario * 0.2
    desconto = 20
imposto_renda = float(imposto_renda)
inss = salario * 0.1
sindicato = salario * 0.03
fgts = salario * 0.11
liquido = salario - (imposto_renda + sindicato)

print(f'\n\nSalário Bruto ({valor_hora} * {horas_trabalhadas})         :RS {salario}')
print(f'(-) IR({desconto}%)                          :RS {imposto_renda}')
print(f'(-) INSS (10%)                       :RS {inss}')
print(f'FGTS (11%)                           :RS {fgts}')
print(f'Total de descontos                   :RS {imposto_renda + sindicato + inss}')
print(f'Salário Líquido                      :RS {liquido}')
