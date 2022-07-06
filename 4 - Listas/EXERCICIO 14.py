"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""
respostas = []

print('RESPONDA AS PERGUNTAS ABAIXO COM "SIM"(S) OU "NÃO"(N).')

try:
  resposta = input('Telefonou para a vítima? ').upper()
  if resposta == 'S' or resposta == 'N':
    if resposta == 'S':
      respostas.append(1)
    else:
      respostas.append(0)
  else:
    print('Você digitou um valor inválido, tente novamente.')
except ValueError:
  print('Você digitou um valor inválido, tente novamente.')

try:
  resposta = input('Esteve no local do crime? ').upper()
  if resposta == 'S' or resposta == 'N':
    if resposta == 'S':
      respostas.append(1)
    else:
      respostas.append(0)
  else:
    print('Você digitou um valor inválido, tente novamente.')
except ValueError:
  print('Você digitou um valor inválido, tente novamente.')


try:
  resposta = input('Mora perto da vítima? ').upper()
  if resposta == 'S' or resposta == 'N':
    if resposta == 'S':
      respostas.append(1)
    else:
      respostas.append(0)
  else:
    print('Você digitou um valor inválido, tente novamente.')
except ValueError:
  print('Você digitou um valor inválido, tente novamente.')

try:
  resposta = input('Devia para a vítima? ').upper()
  if resposta == 'S' or resposta == 'N':
    if resposta == 'S':
      respostas.append(1)
    else:
      respostas.append(0)
  else:
    print('Você digitou um valor inválido, tente novamente.')
except ValueError:
  print('Você digitou um valor inválido, tente novamente.')

try:
  resposta = input('Já trabalhou com a vítima? ').upper()
  if resposta == 'S' or resposta == 'N':
    if resposta == 'S':
      respostas.append(1)
    else:
      respostas.append(0)
  else:
    print('Você digitou um valor inválido, tente novamente.')
except ValueError:
  print('Você digitou um valor inválido, tente novamente.')


if sum(respostas) == 2:
  print('\nSUSPEITO!')
elif (sum(respostas) == 3) or (sum(respostas) == 4):
  print('\nCÚMPLICE!')
elif sum(respostas) == 5:
  print('\nASSASSINO!')
else:
  print('\nINOCENTE!')
