def jogar():

    separacao = '*********************************'
    print(separacao)
    print('Bem vindo ao jogo de Forca!')
    print(separacao)


    palavra_secreta = 'banana'
    letras_acertadas = ['_', '_', '_', '_', '_', '_']
    acertou = False
    enforcado = False

    print(f'\n{letras_acertadas}')

    while not acertou and not enforcado:

        chute = input('Qual a letra? ').lower().strip()

        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                letras_acertadas[index] = letra
            index += 1
        print(letras_acertadas)
        letras_faltando = str(letras_acertadas.count('_'))
        print(f'Ainda falta acetar {letras_faltando}')

print('\nFim do Jogo!')

if __name__ == '__main__':
    jogar()
