
def jogar():

    separacao = '*********************************'
    print(separacao)
    print('Bem vindo ao jogo de Forca!')
    print(separacao)


    palavra_secreta = 'banana'
    acertou = False
    enforcado = False

    while not acertou and not enforcado:

        chute = input('Qual a letra? ').lower().strip()

        index = 1
        for letra in palavra_secreta:
            if chute == letra:
                print(f'Encontrei a letra {letra} na posição: {index}')
            index += 1
        print('Jogando...')

print('\nFim do Jogo!')

if __name__ == '__main__':
    jogar()
