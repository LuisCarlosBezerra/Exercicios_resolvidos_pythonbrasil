"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""
numero1, numero2 = float(input('Digite o primeiro número: ')), float(input('Digite o segundo número: '))
print('Escolha uma operação matemática para ser executada entre os números: "+" , "-", "x" ou "/".')
operação = str(input())

if operação == '+':
    escolha = numero1 + numero2

if operação == '-':
    escolha = numero1 - numero2

if operação == 'x' or operação == "*":
    escolha = numero1 * numero2

if operação == '/':
    escolha = numero1 / numero2

if escolha >= 0:
    sinal = "POSITIVO"
else:
    sinal = "NEGATIVO"

if int(escolha) == escolha:
    dec_ou_int = "INTEIRO"
    resto = divmod(escolha, 2)
    if resto[1] == 0:
        par_ou_impar = 'PAR'
    else:
        par_ou_impar = 'IMPAR'
else:
    dec_ou_int = "DECIMAL"

if dec_ou_int == "INTEIRO":
    print(
        f'O resultado da operação escolhida foi: {escolha} \nEsse número é {par_ou_impar}.\nÉ {sinal}.\nÉ {dec_ou_int}')
else:
    print(f'O resultado da operação escolhida foi: {escolha} \nÉ {sinal}.\nÉ {dec_ou_int}')
