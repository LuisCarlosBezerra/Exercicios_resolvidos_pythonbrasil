"""
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""
print('Olá, em que turno você estuda?')
turno = str(input('Digite M - matutino ; V - vespertino ; N - noturno  '))
turno = turno.upper()

if turno in ['M', 'V', 'N']:
    if turno == 'M':
        print('BOM DIA!')
    if turno == 'V':
        print('BOA TARDE!')
    if turno == 'N':
        print('BOA NOITE!')
else:
    print('VALOR INVÁLIDO!')
