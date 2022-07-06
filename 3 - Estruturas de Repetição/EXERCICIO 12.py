"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
"""
contador = 1
numero = int(input('Digite um número entre 1 e 10 para que seja mostrada a sua tabuada de multiplicação: '))
while (numero < 1) or (numero > 10):
    numero = int(input('Número INVÁLIDO!\nDigite um número entre 1 e 10: '))

for x in range(1, 11, 1):
    produto = x * numero
    print(f'{numero} X {x} = {produto}')
