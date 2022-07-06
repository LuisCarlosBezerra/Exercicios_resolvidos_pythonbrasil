"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""

data = input('INSIRA UMA DATA NO SEGUINTE FORMATO: xx/xx/xxxx  ')
data = data.split('/')
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])

if (1900 < ano <= 2020) and (0 < mes <= 12):
    teste_bisexto = ano % 4
    if teste_bisexto == 0:
        if mes == 2:
            if 0 < dia <= 29:
                print('A DATA DIGITADA É VÁLIDA!')
            else:
                print('DATA INVÁLIDA!')

        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if 0 < dia <= 31:
                print('A DATA DIGITADA É VÁLIDA!')
            else:
                print('DATA INVÁLIDA!')
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if 0 < dia <= 30:
                print('A DATA DIGITADA É VÁLIDA!')
            else:
                print('DATA INVÁLIDA!')

    else:
        if mes == 2:
            if 0 < dia <= 28:
                print('A DATA DIGITADA É VÁLIDA!')
            else:
                print('DATA INVÁLIDA!')

        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if 0 < dia <= 31:
                print('A DATA DIGITADA É VÁLIDA!')
            else:
                print('DATA INVÁLIDA!')
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if 0 < dia <= 30:
                print('A DATA DIGITADA É VÁLIDA!')
            else:
                print('DATA INVÁLIDA!')

else:
    print('DATA INVALIDA!')
