"""
Faça um Programa que peça dois números e imprima a soma.
"""
print("Digite dois números para serem somados.")
# BLOCO QUE TESTA SE O PRIMEIRO NÚMERO É VÁLIDO
teste = False
while teste is False:
    try:
        numero1 = float(input('digite um numero: '))  # RECEBER O PRIMEIRO NUMERO DO USUARIO
        teste = True
    except ValueError:
        print("Digite um valor válido")

# BLOCO QUE TESTA SE O SEGUNDO NÚMERO É VÁLIDO
teste = False
while teste is False:
    try:
        numero2 = float(input('digite o outro numero: '))  # RECEBER O PRIMEIRO NUMERO DO USUARIO
        teste = True
    except ValueError:
        print("Digite um valor válido")

# PROCESSAMENTO
soma = numero1 + numero2  # SENTENÇA QUE REALIZA A SOMA E GUARDA NA VARIÁVEL soma

# SAÍDA DE DADOS
print(f'A soma dos dois números é: {soma}')  # MOSTRA O VALOR DA SOMA DOS DOIS NUMEROS DADOS PELO USUÁRIO
