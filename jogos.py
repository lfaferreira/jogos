import forca
import adivinhacao

def escolhe_jogo():
      separacao = '**********************************'
      print(separacao)
      print('*******Escolha o seu jogo!*******')
      print(separacao)

      print('(1) - Forca\n'
            '(2) - Adivinhação')

      jogo = int(input('Qual jogo?'))

      if jogo == 1:
            print('Jogando forca!')
            forca.jogar()
      elif jogo == 2:
            print('Jogando Adivinhação!')
            adivinhacao.jogar()

#Forma de verificar se o arquivo é o principal ou não.
if(__name__ == '__main__'):
      escolhe_jogo()