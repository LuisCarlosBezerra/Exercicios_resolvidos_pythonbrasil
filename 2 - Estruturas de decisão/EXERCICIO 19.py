"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e
unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades 12 = 1 dezena e 2 unidades
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
numero = int(input('DIGITE UM NUMERO MENOR QUE 1000: '))
centenas_str = divmod(numero, 100)
centenas = centenas_str[0]
dezenas_str = divmod(centenas_str[1], 10)
dezenas = dezenas_str[0]
unidades = dezenas_str[1]

# CENTENAS
if centenas != 0:
    cent_existe = True
    if centenas > 1:
        cent_plural = True
        cent_string = "centenas"
    else:
        cent_plural = False
        cent_string = "centena"
else:
    cent_existe = False

# DEZENAS
if dezenas != 0:
    dez_existe = True
    if dezenas > 1:
        dez_plural = True
        dez_string = "dezenas"
    else:
        dez_plural = False
        dez_string = "dezena"
else:
    dez_existe = False

# UNIDADES
if unidades != 0:
    uni_existe = True
    if unidades > 1:
        uni_plural = True
        uni_string = "unidades"
    else:
        uni_plural = False
        uni_string = "unidade"
else:
    uni_existe = False

# DECISÃO
if cent_existe == 0:
    if dez_existe != 0:
        if uni_existe:
            print(f'O numero dado tem {dezenas} {dez_string} e {unidades} {uni_string}.')
        else:
            print(f'O numero dado tem {dezenas} {dez_string}.')
    else:
        if uni_existe:
            print(f'O numero dado tem {unidades} {uni_string}.')
        else:
            if uni_existe:
                print(f'O numero dado tem {dezenas} {dez_string} e {unidades} {uni_string}.')
            else:
                print('O numero que voce digitou é zero!')

else:
    if dez_existe != 0:
        if uni_existe:
            print(f'O numero dado tem {centenas} {cent_string}, {dezenas} {dez_string} e {unidades} {uni_string}.')
        else:
            print(f'O numero dado tem {centenas} {cent_string} e {dezenas} {dez_string}.')
    else:
        if uni_existe:
            print(f'O numero dado tem {centenas} {cent_string} e {unidades} {uni_string}.')
        else:
            if uni_existe:
                print(f'O numero dado tem {centenas} {cent_string} e {unidades} {uni_string}.')
            else:
                print(f'O numero dado tem {centenas} {cent_string}.')
