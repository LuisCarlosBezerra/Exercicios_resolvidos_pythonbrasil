"""
Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
"""
# TESTANDO SE O VALOR DE ENTRADA É VÁLIDO
validade = False
while validade is False:  # TRY EXCEPT PARA VERIFICAR SE O VALOR DIGITADO É MESMO UM NÚMERO
    try:
        numero = float(input('digite um numero '))  # RECEBER NÚMERO INTEIRO PELO USUÁRIO
        validade = True
    except ValueError:
        print('O valor digitado não é um número')  # MOSTRAR O NÚMERO DIGITADO PELO USUÁRIO

# SAÍDA DE DADOS
print(f'O número digitado foi: {numero}')  # MOSTRAR O NÚMERO DIGITADO PELO USUÁRIO
