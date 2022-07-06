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
reajuste = 0
teste = False
while teste is False:
    try:
        salario = float(input("Digite o valor do seu salário: "))
        if salario > 0:
            teste = True
        else:
            print('Você digitou um valor inválido (zero ou negativo)!')
    except ValueError:
        print('Você digitou um valor inválido! Tente novamente.')

if salario <= 280:
    seletor = 'perfil_1'

if 280 < salario <= 700:
    seletor = 'perfil_2'

if 700 < salario <= 1500:
    seletor = 'perfil_3'

if salario > 1500:
    seletor = 'perfil_4'

dici = {'perfil_1': 20, 'perfil_2': 15, 'perfil_3': 10, 'perfil_4': 5}

reajuste = salario * dici.get(seletor) / 100
print(f'O seu salário era de {"%.2f" % salario} RS.\nVocê recebeu um aumento de {dici.get(seletor)}%, que equivale a '
      f'{"%.2f" % reajuste} RS.\nSeu novo salário é de {"%.2f" % (reajuste + salario)} RS')
