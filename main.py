# Feito Por: Rafahel Costa dos Santos Matias 

# Para testar a forca digite 'main()' no shell e pressione enter

import turtle as t
import random

def d_forca():
   ''' Função que desenha a forca '''
   t.speed(0)
   t.setup(1.0,1.0)

   t.up()
   t.goto(-600,-290)
   t.down()

   t.color('black','saddle brown')

   t.begin_fill()

   t.forward(15)
   t.right(90)
   t.forward(15)
   t.left(90)
   t.forward(20)
   t.left(90)
   t.forward(15)
   t.right(90)
   t.forward(230)
   t.right(90)
   t.forward(15)
   t.left(90)
   t.forward(20)
   t.left(90)
   t.forward(15)
   t.right(90)
   t.forward(15)

   t.left(90)
   t.forward(35)
   t.left(90)
   t.forward(55)
   t.right(90)
   t.forward(5)
   t.right(90)
   t.forward(55)
   t.left(90)

   t.forward(35)
   t.left(90)
   t.forward(55)
   t.right(90)
   t.forward(5)
   t.right(90)
   t.forward(55)
   t.left(90)

   t.forward(35)
   t.left(90)
   t.forward(280)

   t.right(90)
   t.forward(510)
   t.right(90)
   t.forward(230)
   t.left(90)
   t.forward(20)
   t.left(90)
   t.forward(250)
   t.left(90)
   t.forward(530+35)

   t.left(90)
   t.forward(55)
   t.right(90)
   t.forward(5)
   t.right(90)
   t.forward(55)
   t.left(90)

   t.forward(35)
   t.left(90)
   t.forward(55)
   t.right(90)
   t.forward(5)
   t.right(90)
   t.forward(55)
   t.left(90)

   t.forward(35)
   t.left(90)

   t.end_fill()

   t.color('black','white')
   t.up()
   t.goto(-600+60,-290+35)
   t.down()

   t.begin_fill()

   t.forward(180)
   t.left(90)
   t.forward(5)
   t.left(90)
   t.forward(180)
   t.left(90)
   t.forward(5)

   t.end_fill()

   t.up()
   t.goto(-600+60,-290+35+40)
   t.down()
   t.left(90)

   t.begin_fill()

   t.forward(180)
   t.left(90)
   t.forward(5)
   t.left(90)
   t.forward(180)
   t.left(90)
   t.forward(5)
   t.left(90)

   t.end_fill()

   t.color('black')
   t.up()
   t.goto(-600+250-10,-290+625)
   t.down()
   t.goto(-600+250-10,-290+625-37)



def banco(cor, h=0, j=0):
   ''' Função que desenha o banco'''
   t.color(cor)
   t.up()
   t.goto(-600+240+32+h,-290+115+3+j)
   t.down()

   a = 1.8
   
   t.pensize(3)

   t.left(90)
   t.forward(25*a)
   t.left(90)
   t.forward(36*a)
   t.left(90)
   t.forward(25*a)
   t.left(180)
   t.forward(25*a)
   t.left(90)
   t.forward(5*a)
   t.right(90)
   t.forward(5*a)
   t.right(90)
   t.forward(46*a)
   t.right(90)
   t.forward(5*a)
   t.right(90)
   t.forward(5*a)
   t.left(180)





def cabeca1():
   ''' Função que desenha a cabeca '''
   t.pensize(4)
   x = 40
   y = 80
   t.up()
   t.goto(-400+x,120+y)
   t.down()
   t.circle(50)
   return



def corpo1():
   ''' Função que desenha a corpo '''
   x = 40
   y = 80
   t.up()
   t.goto(-400+x,120+y)
   t.down()
   t.goto(-400+x,-100+y)
   

def perna_dir1():
   ''' Função que desenha a perna direita '''
   x = 40
   y = 80
   t.right(70)
   t.forward(100)


def perna_esq1():
   ''' Função que desenha a perna esquerda '''
   x = 40
   y = 80
   t.up()
   t.goto(-400+x,-100+y)
   t.down()
   t.right(40)
   t.forward(100)


def braco_esq1():
   ''' Função que desenha a braço esquerdo '''
   x = 40
   y = 80
   t.up()
   t.goto(-400+x,50+y)
   t.down()
   t.left(110)
   t.right(130)
   t.forward(80)


def braco_dir1():
   ''' Função que desenha a braço direito '''
   x = 40
   y = 80
   t.up()
   t.goto(-400+x,50+y)
   t.down()
   t.left(80)
   t.forward(80)
   t.left(50)

def move_banco():
   ''' Função que faz o banco se mover quando perde o jogo '''
   # O banco com a cor branca faz o banco ser apagado           
   banco('white')
   t.right(20)
   banco('black')
   banco('white')
   t.right(20)
   banco('black')
   banco('white')
   t.right(30)
   banco('black')
   banco('white')
   t.right(20)
   banco('black')
   banco('white')
   t.right(20)
   banco('black',33)
   banco('white',33)
   t.right(20)
   banco('black',33,-10)
   banco('white',33,-10)
   t.right(20)
   banco('black',33,-75)
   banco('white',33,-75)
   t.right(30)
   banco('black',53,-75)
               
   t.left(180)
   t.up()
   x = 40
   y = 80
   t.goto(-400+x,-100+y)
   t.down()
   perna_dir1()
   t.right(180)
               
   





def forca():
   ''' Funcão do jogo da forca. Jogo com 30 palavras divididas em 5 temas '''

   while True:
      # Nessa parte escolhe o tema
   
      musculo=['peitoral','deltoide','dorsal','panturrilha','quadriceps','biceps']

      time=['real','flamengo','botafogo','fluminense','palmeiras','corinthians']
      
      cidade=['rio','londres','sidney','chicago','paris','tokio']

      planeta=['marte','saturno','jupter','urano','netuno','terra']
      
      comida=['hamburguer','pizza','sushi','strogonff','massa','sanduiche']

      palavras=[musculo, time, cidade, planeta, comida]

      ini2=input('Escolha um desses temas digitando o respectivo numero \n(caso queira parar o jogo precione enter)\n\n Musculos 0, Times 1, Cidades 2, Planetas 3  ou Comidas 4: ')
      
      if ini2 == '': break
      
      ini2 = int(ini2)
      
      
      contador = 0
      
      while True:
         # Nessa parte a palavra é escolhida de forma aleatoria e desenha a forca e o banco para dar inicio ao jogo
         w=palavras[ini2]
         palavra = random.choice(w)
         if contador == 6: break
         if contador >= 1:
            print()
            ini3 = input('Enter se deseja continuar com esse tema, \ncaso contrario aperte espaço e enter para confirmar: ')
            print()
            if ini3 == ' ': break
         ini = input('\nEnter para iniciar: ')
         print()
         contador += 1
         t.reset()
         t.hideturtle()
         d_forca()
         banco('black')
         print('A palavra tem',len(palavra),'letras')
         print()
         cabeca = 0
         corpo = 0
         perna_dir = 0
         perna_esq = 0
         braco_esq = 0
         braco_dir = 0
         erros = 0
         letras_erradas = ''
         acertos = 0
         todas_letras = ''
         palavra_certa = '-' * len(palavra)
         chances = 6
         while True:
            # Nessa parte o jogo é iniciado
            if erros == 6:
               print()
               print(f'A palavra correta é "{palavra}"')
               print()
               print('Game over')
               print()
               break
            
            if acertos == len(palavra):
               print()
               print('Congratulation')
               print()
               break
            
            letra = input('Digite uma letra: ')
            if letra in todas_letras:
               print()
               print('Tente outra letra, essa já foi testada.')
               print()
               continue
            todas_letras += letra
            
            if letra not in palavra:
               # desenha as linhas do lado da forca as as letras em cima para mostrar o erro
               erros += 1
               letras_erradas += (letra + ' ')
               print()
               print('Palavra: ',palavra_certa)
               print('Erros:   ',letras_erradas)
               chances -= 1
               print('Você tem',chances,'chance(s)')
               print()
            
            if letra in palavra:
               indice_lista = []
               aux = 0
               cont_letras = palavra.count(letra)
               # Para palavra com letra repetida
               if cont_letras > 1:
                  while cont_letras > 0:
                     w = palavra.find(letra,aux)
                     indice_lista.append(w)
                     aux = w + 1
                     cont_letras -= 1
                     acertos += 1
                  for ind in indice_lista:
                     palavra_certa_aux = palavra_certa
                     palavra_certa = ''
                     cont = 0
                     for i in palavra_certa_aux:
                        if cont == ind:
                           palavra_certa += letra
                        else:
                           palavra_certa += i
                        cont += 1
               # Para palavra sem letra repetida
               elif cont_letras == 1:
                  acertos += 1
                  indice = palavra.find(letra)
                  palavra_certa_aux = palavra_certa
                  palavra_certa = ''
                  cont = 0
                  for i in palavra_certa_aux:
                     if cont == indice:
                        palavra_certa += letra
                     else:
                        palavra_certa += i
                     cont += 1
               print()
               print('Palavra: ',palavra_certa)
               print('Erros: ',letras_erradas)
               print('Você tem',chances,'chance(s)')
               print()
            
            # Nessa parte é desenhada as partes de corpo quando o usuario erra
            if erros == 1 and cabeca == 0:
               cabeca1()
               cabeca = 1
            
            if erros == 2 and corpo == 0:
               corpo1()
               corpo = 1
               
            if erros == 3 and perna_dir == 0:
               perna_dir1()
               perna_dir = 1

            if erros == 4 and perna_esq == 0:
               perna_esq1()
               perna_esq = 1

            if erros == 5 and braco_esq == 0:
               braco_esq1()
               braco_esq = 1

            if erros == 6 and braco_dir == 0:
               braco_dir1()
               braco_dir = 1
               
               move_banco()
               



def main():
   forca()
