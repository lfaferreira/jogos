import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = define_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    exibe_espaços_das_letras_da_palavra_secreta(letras_acertadas)
    verifica_resultado_da_partida(loop_do_jogo(palavra_secreta, letras_acertadas), palavra_secreta)
    print('\nFim do Jogo!')

def imprime_mensagem_abertura():
    separacao = '*********************************'
    print(separacao)
    print('Bem vindo ao jogo de Forca!')
    print(separacao)

def define_palavra_secreta(primeira_linha_valida = 0):
    palavras = leitura_de_arquivo()
    return palavras[random.randrange(primeira_linha_valida, len(palavras))]

def leitura_de_arquivo(nome_arquivo='frutas.txt'):
    arquivo = open(nome_arquivo, 'r')
    palavras = [linha.strip().lower() for linha in arquivo]
    arquivo.close()
    return palavras

def inicializa_letras_acertadas(palavra_secreta):
    return ['_' for letra in palavra_secreta]

def exibe_espaços_das_letras_da_palavra_secreta(letras_acertadas):
    print(f'\n{letras_acertadas}'
          f'\n')

def loop_do_jogo(palavra_secreta, letras_acertadas):
    acertou = False
    enforcado = False
    tentativas = 0

    while not acertou and not enforcado:

        chute = entrada_do_usuario()

        if chute in palavra_secreta:
            preenche_letras_acertadas(palavra_secreta, chute, letras_acertadas)
        else:
            tentativas += 1
            print(f'Eita, errase! Falta {7 - tentativas} tentativas.')
            desenha_forca(tentativas)

        verifica_estado_atual_do_jogo(letras_acertadas)

        if tentativas == 7 or '_' not in letras_acertadas:
            return letras_acertadas

def entrada_do_usuario():
    return input('Qual a letra? ').lower().strip()

def preenche_letras_acertadas(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def verifica_estado_atual_do_jogo(letras_acertadas):
    print(f'{letras_acertadas}')
    letras_faltando = str(letras_acertadas.count('_'))
    print(f'Ainda falta acetar {letras_faltando}'
          f'\n')

def verifica_resultado_da_partida(letras_acertadas, palavra_secreta):
    if '_' not in letras_acertadas:
        menssagem_vitoria()
    else:
        menssagem_derrota(palavra_secreta)

def menssagem_vitoria():
    print('Parabéns! Você ganhou o jogo!')
    trofeu()

def trofeu():
    print("       ___________   ")
    print("      '._==_==_=_.'  ")
    print("      .-\\:      /-. ")
    print("     | (|:.     |) | ")
    print("      '-|:.     |-'  ")
    print("        \\::.    /   ")
    print("         '::. .'     ")
    print("           ) (       ")
    print("         _.' '._     ")
    print("        '-------'    ")

def menssagem_derrota(palavra_secreta):
    print('Você perdeu! '
          f'A palavra secreta era: {palavra_secreta}'
          f'\n')
    caveira()

def caveira():
    print('                      :::!~!!!!!:.')
    print('                  .xUHWH!! !!?M88WHX:.')
    print('                .X*#M@$!!  !X!M$$$$$$WWx:.')
    print('               :!!!!!!?H! :!$!$$$$$$$$$$8X:')
    print('              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:')
    print('             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!')
    print('             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!')
    print('               !:~~~ .:!M"T#$$$$WX??#MRRMMM!')
    print('               ~?WuxiW*`   `"#$$$$8!!!!??!!!')
    print('             :X- M$$$$       `"T#$T~!8$WUXU~')
    print('            :%`  ~#$$$m:        ~!~ ?$$$$$$')
    print('          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"')
    print('.....   -~~:<` !    ~?T#$$@@W@*?$$      /`')
    print('W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :')
    print('#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`')
    print(':::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~')
    print('.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `')
    print('Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!')
    print('$R@i.~~ !     :   ~$$$$$B$$en:``')
    print('?MXT@Wx.~    :     ~"##*$$$$M~')

if __name__ == '__main__':
    jogar()
