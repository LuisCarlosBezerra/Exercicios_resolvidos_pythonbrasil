"""
Faça um Programa que converta metros para centímetros.
"""
# TESTANDO A VALIDADE DA VARIÁVEL INFORMADA
teste = False
while teste is False:
    try:
        metros = float(input(
            'Digite o valor em metros para ser convertido em centimetros: '))  # RECEBENDO E GUARDANDO O VALOR DE
        # METROS NUMA VARIÁVEL REAL
        teste = True
    except ValueError:
        print("Valor digitado não é um número")

# PROCESSAMENTO
centimetros = metros * 100

# SAÍDA DE DADOS
print(f'{metros:.2f} metros é equivalente a {centimetros:.2f} centímetros.')
