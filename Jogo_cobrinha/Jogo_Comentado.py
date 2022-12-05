import pygame
from pygame.locals import*
from sys import exit
from random import randint

# iniciando pygame
pygame.init()
pygame.display.set_caption('SNAKE GAME')

#Criando uma tela de jogo
#Variaveis

#Musica

pygame.mixer.music.set_volume(0.5)
musica_fundo = pygame.mixer.music.load('Fundo.wav')
pygame.mixer.music.play(-1)
coin = pygame.mixer.Sound('coin.wav')
coin.set_volume(1)




font = pygame.font.SysFont('arial', 40, True, True)
pontos = 0

# Variaveis do tamanho da tela
x = 800
y = 600

# Variaveis para posição do ret do player
ret_x = x/2
ret_y = y/2

#Variaveis de moviemnto do player
velocidade = 10
x_controle = 20
y_controle = 0

# Variaveis para posição do ret do inimigo para uma posição aleatoria import random
ini_x = randint(40, 600)
ini_y = randint(50, 430)

tela = pygame.display.set_mode((x, y))

#variavel para usar o tempo da aplicação
relogio = pygame.time.Clock()

comprimento_incial = 3

morreu = False

#Lista com os valores de lista_cabeca armazenados
lista_cobra = []

#função para fazer a cobra aumentar seu corpo
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))



def reiniciar_jogo():
    global pontos, comprimento_incial, ret_x, ret_y, lista_cabeca, lista_cobra, ini_x, ini_y,morreu
    pontos = 0
    comprimento_incial = 5
    ret_x = x/2
    ret_y = y/2
    lista_cobra = []
    lista_cabeca = []
    ini_x = randint(40, 600)
    ini_y = randint(50, 430)
    morreu = False



# Comando para deixar o jogo em um loop infinito e fechar a tela de jogo 

while True:
    #aplicando o tempo de aplicação por frames
    relogio.tick(20)
    #tela.fill acada interação do loop infinito a tela é preenchida com branco
    tela.fill((0,0,255))
    mensagem = f'PONTOS: {pontos}'
    texto_formatado = font.render(mensagem, False, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() 
            exit()
# Movimento do player
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

    ret_x = ret_x + x_controle
    ret_y = ret_y + y_controle


        

# na primeira tupla o 'ret_x'e 'ret_y ' representam a posição do rect
# Já na segunda o tamanho do rect
    player = pygame.draw.rect(tela, (255,0,255), (ret_x, ret_y, 20, 20)) 
    inimigo = pygame.draw.rect(tela, (255,255,255), (ini_x, ini_y, 20, 20))

#Condição para verificar se o player colidir com inimigo a posição do inimigo ira mudar para uma aleatoria
    if player.colliderect(inimigo):
        ini_x = randint(40, 600)
        ini_y = randint(50, 430)
        pontos = pontos + 1
        coin.play()
        comprimento_incial = comprimento_incial + 1

#Criando uma lista e armazenando o X e Y do player com  '.append' 
    lista_cabeca = []
    lista_cabeca.append(ret_x)
    lista_cabeca.append(ret_y)

 #Colocando os valores armazenados em lista_cobra e puxando eles na funçao aumenta_cobra   
    lista_cobra.append(lista_cabeca)


#Condição para checar se a conra encostou no proprio corpo 
    if lista_cobra.count(lista_cabeca) > 1:
        morreu = True
#Formatando texto de morte
        fonte2= pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'GAME OVER!! Pressione a tecla R para jogar novamente!'
        texto_formatado = fonte2.render(mensagem, True, ((0,0,0)))
        ret_texto = texto_formatado.get_rect()

 # Tela de game over      
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        #Chamando função reiniciar_jogo la em cima 
                        reiniciar_jogo()
            #Formatando posição do texto de game over
            ret_texto.center = (x//2, y//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

#Configuração do layout se a cobra sair d layout voltar para outro lado
    if ret_x > x:
        ret_x = 0
    if ret_x < 0:
        ret_x = x
    if ret_y < 0:
        ret_y = y
    if ret_y > y:
        ret_y = 0

    if len(lista_cobra) > comprimento_incial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)
        

    tela.blit(texto_formatado, (540, 40))
#Regras de jogo
    if pontos == 30:
        pontos = 'YOU WIN'
        pygame.quit() 
        

    
    pygame.display.update()