"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""
print("Calcule o seu salário através das horas: ")

teste = False
while teste is False:
    try:
        valorhora, horas = float(input('Digite o valor da sua hora trabalhada: ')), float(
            input('Digite quantas horas trabalhadas no mês: '))
        teste = True
    except ValueError:
        print("Você digitou um valor inválido!")

salario = horas * valorhora
print(f'Seu salário será de {"%.2f" % salario} R$.')
