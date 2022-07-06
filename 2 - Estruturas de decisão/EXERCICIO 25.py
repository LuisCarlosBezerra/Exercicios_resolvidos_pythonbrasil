"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
resposta = ' '
contador = 0

print('Responda as seguintes perguntas com "S" para SIM ou "N" para NÃO. ')
print('Telefonou para a vítima? ')
resposta = str(input())
resposta = resposta.upper()
if resposta == 'S':
    contador = contador + 1
resposta == ' '

print('Esteve no local do crime? ')
resposta = str(input())
resposta = resposta.upper()
if resposta == 'S':
    contador = contador + 1
resposta == ' '

print('Mora perto da vítima? ')
resposta = str(input())
resposta = resposta.upper()
if resposta == 'S':
    contador = contador + 1
resposta == ' '

print('Devia para a vítima? ')
resposta = str(input())
resposta = resposta.upper()
if resposta == 'S':
    contador = contador + 1
resposta == ' '

print('Já trabalhou com a vítima? ')
resposta = str(input())
resposta = resposta.upper()
if resposta == 'S':
    contador = contador + 1
resposta == ' '

if contador < 2:
    print('INOCENTE')

if contador == 2:
    print('SUSPEITO')

if 3 <= contador <= 4:
    print('CÚMPLICE')

if contador == 5:
    print('CULPADO')
