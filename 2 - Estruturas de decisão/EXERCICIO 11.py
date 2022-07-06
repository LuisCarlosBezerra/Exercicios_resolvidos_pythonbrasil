"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver
o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no
salário atual:

salários até RS 280,00 (incluindo) : aumento de 20%
salários entre RS 280,00 e RS 700,00 : aumento de 15%
salários entre RS 700,00 e RS 1500,00 : aumento de 10%
salários de RS 1500,00 em diante : aumento de 5%

Após o aumento ser realizado, informe na tela:

o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
teste = False
while teste is False:
    try:
        salario = float(input('Digite o valor do salário do funcionário: '))
        if salario > 0:
            teste = True
        else:
            print('Você digitou um valor inválido (zero ou negativo). Tente novamente.')
    except ValueError:
        print('Você digitou um valor inválido! Tente novamente.')

reajuste = 0

if salario <= 280:
    reajuste = salario * 1.2
    print(
        f'O seu salário era de {"%.2f" % salario} RS.\nVocê recebeu um aumento de 20%, que equivale a '
        f'{"%.2f" % (reajuste - salario)} RS.\nSeu novo salário é de {"%.2f" % reajuste} RS')
if 280 < salario <= 700:
    reajuste = salario * 1.15
    print(
        f'O seu salário era de {"%.2f" % salario} RS.\nVocê recebeu um aumento de 15%, que equivale a '
        f'{"%.2f" % (reajuste - salario)} RS.\nSeu novo salário é de {"%.2f" % reajuste} RS')
if 700 < salario <= 1500:
    reajuste = salario * 1.1
    print(
        f'O seu salário era de {"%.2f" % salario} RS.\nVocê recebeu um aumento de 10%, que equivale a '
        f'{"%.2f" % (reajuste - salario)} RS.\nSeu novo salário é de {"%.2f" % reajuste} RS')
if salario > 1500:
    reajuste = salario * 1.05
    print(
        f'O seu salário era de {"%.2f" % salario} RS.\nVocê recebeu um aumento de 5%, que equivale a '
        f'{"%.2f" % (reajuste - salario)} RS.\nSeu novo salário é de {"%.2f" % reajuste} RS')
