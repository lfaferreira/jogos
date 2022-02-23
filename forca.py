def jogar():

    separacao = '*********************************'
    print(separacao)
    print('Bem vindo ao jogo de Forca!')
    print(separacao)


    palavra_secreta = 'banana'
    letras_acertadas = ['_' for letra in palavra_secreta]

    acertou = False
    enforcado = False
    tentativas = 0

    print(f'\n{letras_acertadas}'
          f'\n')

    while not acertou and not enforcado:

        chute = input('Qual a letra? ').lower().strip()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas += 1
            print(f'Eita, errase! Falta {6 - tentativas} tentativas.')

        print(f'{letras_acertadas}')
        letras_faltando = str(letras_acertadas.count('_'))
        print(f'Ainda falta acetar {letras_faltando}'
              f'\n')

        if tentativas == 6 or '_' not in letras_acertadas:
            break

    if '_' not in letras_acertadas:
        print('Parabéns!!! Você ganhou.')
    else:
        print('Você perdeu. Tente novamente!')

    print('Fim do Jogo!')

if __name__ == '__main__':
    jogar()
