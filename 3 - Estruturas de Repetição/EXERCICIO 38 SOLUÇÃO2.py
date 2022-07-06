"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário.
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
"""
# SOLUÇÃO 02 - PERMITE A ENTRADA DO SALÁRIO INICIAL DO FUNCIONÁRIO

while True:
  try:
    salario_inicial = float(input('Entre com o salário de admissão do funcionário: '))
    if salario_inicial > 0:
      break
    else:
      print('Você digitou um valor nulo ou negativo, tente novamente.')
  except ValueError:
    print('Você digitou um valor inválido, tente novamente.')

while True:
  try:
    ano_atual = int(input('Entre com o ano atual do funcionário: '))
    if ano_atual > 1996:
      break
    else:
      print('Você digitou um ano inferior ao de entrada do funcionário na empresa (1996), tente novamente.')
  except ValueError:
    print('Você digitou um valor inválido, tente novamente.')

salario_atual = salario_inicial
aumento = 0.015

for i in range(1997, ano_atual + 1, 1):
  salario_atual = salario_atual * (1 + aumento)
  aumento *= 2

print(f'O valor do salário atual do funcionário é de {"%.2f" % salario_atual} RS')
