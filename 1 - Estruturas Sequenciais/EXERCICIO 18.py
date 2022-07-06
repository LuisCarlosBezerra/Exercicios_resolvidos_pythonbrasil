"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em
Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). """
teste = False
while teste is False:
    try:
        tamanho_arquivo = float(input('Insira o tamanho do arquivo que será baixado '))
        velocidade_internet = float(input('Qual é a velocidade da internet em Mbps? '))
        if (tamanho_arquivo <= 0) or (velocidade_internet <= 0):
            print("Você digitou um valor inválido. Tente novamente.")
        else:
            teste = True
    except ValueError:
        print("Você digitou um valor inválido. Tente novamente.")

velocidade_MB = (0.125 * velocidade_internet)
tempo_download = tamanho_arquivo / velocidade_MB
tempo_minutos = divmod(tempo_download, 60)
# print(tempo_minutos)

if tempo_minutos[0] == 0:
    print(f'O tempo aproximado para download do seu arquivo será de {"%.0f" % tempo_minutos[1]} segundos.')

else:
    if tempo_minutos[0] == 1:
        print(
            f'O tempo aproximado para download do seu arquivo será de {"%.0f" % tempo_minutos[0]} minuto e '
            f'{"%.0f" % tempo_minutos[1]} segundos.')
    else:
        print(
            f'O tempo aproximado para download do seu arquivo será de {"%.0f" % tempo_minutos[0]} minutos e '
            f'{"%.0f" % tempo_minutos[1]} segundos.')
