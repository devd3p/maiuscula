def tem_maiusculas(palavra):
    palavra = input('Digite uma palavra: ')
    for letra in palavra:
        if letra == letra.upper():
            return f'{palavra} tem maiúscula.'
    return f'{palavra} não tem maiúscula.'