import pygame
from pygame.locals import *
from sys import exit
from random import randint  #responsavel pela a colisao

pygame.init()
#...............Para colocar musica no jogo................
pygame.mixer.music.set_volume(0.2)#para controlar o volume do jogo
musica_de_fundo = pygame.mixer.music.load('smw_course_clear.wav')#musica tirada no site da musica dos jogos
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')# o som da colisao do jogo
largura= 640
altura=480

#OBS: m e x , z e y
m=largura/2 #representa as medidas de x
z=altura/2 # representa as medidas de y

#para o retengulo azul conseguir mudar lugar
x_azul=randint(40,600)
y_azul=randint(50,430)
#........Para o texto-PONTOS.............................
fontre = pygame.font.SysFont('gabriola',40,True,True)  #para o texto no ecra de pontos"Pontos"
                                            #3º parametro e seker para estar em negrito ou nao
                                            #4º parametro Italico  ou nao
pontos=0
tela = pygame.display.set_mode((largura,altura))#representa a tela
pygame.display.set_caption('Elmer Santios')#para dar o nome ao jogo
#relogio = pygame.time.clock()

while True:
    #relogio.tick(30)
    tela.fill((0,0,0))#recebe essa tupla , ou seja a cor que a nossa tela fica
    mensagem= f'Pontos :{pontos}'
    texto_formatado=fontre.render(mensagem,True,(255,255,255))#2 parametro e se ker pixelado e a 3 e a cor-Branca
    for event in pygame.event.get() :#e o loop ke controla qual evento que ocorreu no jogo
        if event.type == QUIT:
            pygame.quit()
            exit()
            #............Controlando os Objetos.............
            #.......as teclas utilizadas para jogar sao W,A,S,D.................................


        if event.type == KEYDOWN:#se apertar qualquer tecla do meu teclado quero que acontece alguma coisa
            if event.key == K_a:
                m=m-20
            if event.key == K_d:
                m = m + 20
            if event.key == K_w:
                z = z - 20
            if event.key == K_s:
                    z = z + 20
                    """
    if pygame.key.get_pressed()[K_a]:
        m = m-20
    if pygame.key.get_pressed()[K_d]:
         m = m + 20
    if pygame.key.get_pressed()[K_w]:
        z= z - 20
    if pygame.key.get_pressed()[K_s]:
        z = z + 20   """

    #ao lado m
#para cima z
            #desenhar figuras na tela
    ret_vermelha=pygame.draw.rect(tela,(138,43,226),(m,z,40,50))#desenho de um quadrado
    ret_azul=pygame.draw.rect(tela,(255,69,0),(x_azul,y_azul,40,50))
   # pygame.draw.circle(tela,(0,0,255),(300,260),40)#o ultimo parametro e o raio
   # pygame.draw.line(tela,(255,255,0),(390,0),(390,600),5)# recebe dois parametros um inicial e um final e o ultimo parametro e a esessura
    #z= z+1
    #condicao para o movimento
    #if z >=altura:
       # z=0
    #z= z+5
    #..............................................................
    #---------------------------------Para a colisao-----------------------------
    if ret_vermelha.colliderect(ret_azul):#vai verificar se o quadrado esta colidir com o outro(ou seja onde acontece a colisao)
        x_azul=randint(40,600)
        y_azul=randint(50,430)
        #fazendo colidir com o outro quadrado
        print("Voce espancou em mim")
        pontos= pontos + 1
        barulho_colisao.play()
    tela.blit(texto_formatado,(400,40))
    pygame.display.update()#linha codigo para a tela do jogo atulizar

