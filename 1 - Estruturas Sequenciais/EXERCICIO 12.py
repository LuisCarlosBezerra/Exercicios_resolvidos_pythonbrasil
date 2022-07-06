"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58
"""
teste = False
while teste is False:
    try:
        altura = float(input('Digite a sua altura: '))
    except ValueError:
        print("Você digitou um valor inválido. Tente novamente!")

    if (altura >= 1.00) & (altura <= 2.40):
        teste = True
    else:
        if altura < 0:
            print("Voce digitou um valor negativo. Não há altura negativa, tente novamente!")
        else:
            print("Você digitou um valor inválido. Tente um valor entre 1.00 e 2,40 metros!")

print(f'O seu peso ideal é: {"%.2f" % ((72.7 * altura) - 58)} quilos')
