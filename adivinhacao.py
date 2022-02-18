import random

def jogar():

    separacao = '*********************************'
    print(separacao)
    print('Bem vindo ao jogo de Adivinhação!')
    print(separacao)

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 3
    rodada = 1
    pontos = 1000

    print('Qual nivel de dificuldade?')
    print('(1) - Facil\n'
          f'(2) - Médio\n'
          f'(3) - Dificil')
    nivel = int(input('Define o nivel: '))
    print(separacao)

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas +1):
        print(f'\nTentativa {rodada} de {total_de_tentativas}')

        chute = int(input("Digite o seu número entre 1 e 100: "))
        print(f'Você digitou: {chute}')

        if chute < 1 or chute >100:
            print('Você digitar um número entre 1 e 100!')
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print('\nVocê acertou!\n'
                  f'Sua pontuação foi {pontos}!')
            break
        else:
            if maior:
                print('Você errou! O seu chute foi maior do que o número secreto.')
            elif menor:
                print('Você errou! O seu chute foi menor do que o número secreto.')
            if rodada == total_de_tentativas:
                print(f'\nO número secreto era {numero_secreto}. Você fez {pontos} pontos!')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos-= pontos_perdidos

    print('Fim do jogo')

if(__name__ == '__main__'):
    jogar()