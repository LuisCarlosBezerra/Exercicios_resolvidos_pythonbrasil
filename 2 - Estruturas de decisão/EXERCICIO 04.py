"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
vogais = ['A', 'E', 'I', 'O', 'U']
consoantes = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
letra = str(input('Digite uma letra! '))
letra = letra.upper()
if letra in vogais:
    print('Você digitou uma VOGAL!')
elif letra in consoantes:
    print('Você digitou uma CONSOANTE!')
else:
    print('Você digitou um valor INVÁLIDO!')
