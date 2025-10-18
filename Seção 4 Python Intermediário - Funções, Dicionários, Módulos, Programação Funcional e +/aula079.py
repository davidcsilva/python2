'''
131. Exemplo de uso do tipo set

'''

# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('PARABÉNS')
        break

    print(letras)
