"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e
unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades 12 = 1 dezena e 2 unidades
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
while True:
    try:
        numero = int(input('Digite um valor de até 3 algarismos (entre 0 e 999):  '))
        if 0 <= numero <= 999:
            break
        elif numero >= 1000:
            print('Digite um valor dentro do intervalo informado. Tente novamente.')
        else:
            print('Digite um valor positivo. Tente novamente.')
    except ValueError:
        print('Você digitou um valor inválido. Tente novamente.')

# CENTENAS
centenas = numero // 100
if centenas == 1:
    centenas_string = 'centena'
elif centenas > 1:
    centenas_string = 'centenas'
else:
    centenas_string = ''

# DEZENAS
dezenas = numero - (centenas * 100)
dezenas = dezenas // 10
if dezenas == 1:
    dezenas_string = 'dezena'
elif dezenas > 1:
    dezenas_string = 'dezenas'
else:
    dezenas_string = ''

# UNIDADES
unidades = numero - (centenas * 100) - (dezenas * 10)
if unidades == 1:
    unidades_string = 'unidade'
elif unidades > 1:
    unidades_string = 'unidades'
else:
    unidades_string = ''

# print(centenas , dezenas , unidades)
# SAÍDA

if (centenas > 0) and (dezenas > 0) and (unidades > 0):
    print(f'{centenas} {centenas_string}, {dezenas} {dezenas_string} e {unidades} {unidades_string}.')

elif (centenas > 0) and (dezenas > 0) and (unidades == 0):
    print(f'{centenas} {centenas_string} e {dezenas} {dezenas_string}. ')

elif (centenas > 0) and (dezenas == 0) and (unidades > 0):
    print(f'{centenas} {centenas_string} e {unidades} {unidades_string}. ')

elif (centenas == 0) and (dezenas > 0) and (unidades > 0):
    print(f'{dezenas} {dezenas_string} e {unidades} {unidades_string}.')

elif (centenas == 0) and (dezenas > 0) and (unidades == 0):
    print(f'{dezenas} {dezenas_string}.')

elif (centenas == 0) and (dezenas == 0) and (unidades > 0):
    print(f'{unidades} {unidades_string}.')

elif (centenas > 0) and (dezenas == 0) and (unidades == 0):
    print(f'{centenas} {centenas_string}.')
