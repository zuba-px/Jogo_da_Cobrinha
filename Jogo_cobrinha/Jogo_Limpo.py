import pygame
from pygame.locals import*
from sys import exit
from random import randint

# iniciando pygame
pygame.init()
pygame.display.set_caption('SNAKE GAME')



#Musica

pygame.mixer.music.set_volume(0.5)
musica_fundo = pygame.mixer.music.load('Fundo.wav')
pygame.mixer.music.play(-1)
coin = pygame.mixer.Sound('coin.wav')
coin.set_volume(1)




font = pygame.font.SysFont('arial', 40, True, True)
pontos = 0


x = 800
y = 600


cobra_x = x/2
cobra_y = y/2

velocidade = 10
x_controle = 20
y_controle = 0

comida_x = randint(40, 600)
comida_y = randint(50, 430)

tela = pygame.display.set_mode((x, y))

relogio = pygame.time.Clock()

comprimento_incial = 3

morreu = False

lista_cobra = []

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))



def reiniciar_jogo():
    global pontos, comprimento_incial, cobra_x, cobra_y, lista_cabeca, lista_cobra, comida_x, comida_y,morreu
    pontos = 0
    comprimento_incial = 5
    cobra_x = x/2
    cobra_y = y/2
    lista_cobra = []
    lista_cabeca = []
    comida_x = randint(40, 600)
    comida_y = randint(50, 430)
    morreu = False




while True:

    relogio.tick(20)

    tela.fill((0,0,255))
    mensagem = f'PONTOS: {pontos}'
    texto_formatado = font.render(mensagem, False, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() 
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = - velocidade
                    y_controle = 0

            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle =  velocidade
                    y_controle = 0

            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = - velocidade
                    x_controle = 0

            if event.key == K_s:
                if y_controle == - velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    cobra_x = cobra_x + x_controle
    cobra_y = cobra_y + y_controle



    player = pygame.draw.rect(tela, (255,0,255), (cobra_x, cobra_y, 20, 20)) 
    inimigo = pygame.draw.rect(tela, (255,0,0), (comida_x, comida_y, 20, 20))

    if player.colliderect(inimigo):
        comida_x = randint(40, 600)
        comida_y = randint(50, 430)
        pontos = pontos + 1
        coin.play()
        comprimento_incial = comprimento_incial + 1

    lista_cabeca = []
    lista_cabeca.append(cobra_x)
    lista_cabeca.append(cobra_y)

    lista_cobra.append(lista_cabeca)



    if lista_cobra.count(lista_cabeca) > 1:
        morreu = True

        fonte2= pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'GAME OVER!! Pressione a tecla R para jogar novamente!'
        texto_formatado = fonte2.render(mensagem, True, ((0,0,0)))
        ret_texto = texto_formatado.get_rect()

 
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                    
                        reiniciar_jogo()
         
            ret_texto.center = (x//2, y//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    if cobra_x > x:
        cobra_x = 0
    if cobra_x < 0:
        cobra_x = x
    if cobra_y < 0:
        cobra_y = y
    if cobra_y > y:
        cobra_y = 0

    if len(lista_cobra) > comprimento_incial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)
        

    tela.blit(texto_formatado, (540, 40))

  

  
        

    
    pygame.display.update()