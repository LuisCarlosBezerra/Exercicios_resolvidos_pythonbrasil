"""
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""
print('Olá, em que turno você estuda?')

teste = False
while teste is False:
    try:
        turno = str(input('Digite M - matutino ; V - vespertino ; N - noturno  '))
        turno = turno.upper()
        if turno in ['M', 'V', 'N']:
            teste = True
        else:
            print('Digite um valor válido!')
    except ValueError:
        print('Digite um valor válido!')


# ESTRUTURA SIMILAR A CASE
def matutino():
    print('BOM DIA!')


def vespertino():
    print('BOA TARDE!')


def noturno():
    print('BOA NOITE!')


# DICIONÁRIO
option = {'M': matutino, 'V': vespertino, 'N': noturno}

option.get(turno)()
