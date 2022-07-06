"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
# TESTANDO SE O USUÁRIO DIGITOU UM VALOR FLOAT
teste = False
while teste is False:
    try:
        altura = float(input('Digite a sua altura: '))
    except ValueError:
        print("Você digitou um valor inválido. Tente novamente.")

    # FILTRANDO OS VALORES ACEITÁVEIS
    if (altura >= 1.00) & (altura <= 2.40):
        teste = True
    else:
        if altura < 0:
            print("Você digitou um valor negativo! Tente novamente.")
        else:
            print("Você digitou um valor inválido. Tente um valor entre 1,00 e 2,40 metros.")

# IDENTIFICANDO O SEXO DO USUÁRIO E FILTRANDO SOMENTE CARACTERES VÁLIDOS
sexo = input('Digite H para HOMEM ou M para MULHER:  ').upper()
while sexo != 'H' and sexo != 'M':
    sexo = input('Digite um sexo válido! ').upper()

# PROCESSAMENTO E RESULTADOS, DE ACORDO COM O SEXO
if sexo == 'H':
    print(f'O seu peso ideal é: {"%.2f" % ((72.7 * altura) - 58)} quilos')

if sexo == 'M':
    print(f'O seu peso ideal é: {"%.2f" % ((62.1 * altura) - 44.7)} quilos')
