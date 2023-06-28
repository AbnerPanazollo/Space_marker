import pygame
import os
from tkinter import simpledialog

pygame.init()
tamanho = (800,563)
tela = pygame.display.set_mode(tamanho)
nave = pygame.image.load("space.png")
fundo = pygame.image.load("bg.jpg")
branco = (255,255,255)
estrelas={}
pontos=[]
superficie_desenho = pygame.Surface(tamanho)
pygame.display.set_caption("Space Marker")
pygame.display.set_icon(nave)
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
fonte = pygame.font.Font(None, 20)

def limpaTela():
    os.system("cls")
def apagar_arquivo(nome_arquivo):
    try:
        if os.path.exists(nome_arquivo):
            os.remove(nome_arquivo)
            print(f"Arquivo '{nome_arquivo}' apagado com sucesso!")
        else:
            print(f"Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao apagar o arquivo: {str(e)}")
def desenha_estrela():
    for nome,pos in estrelas.items():
        pygame.draw.circle(tela,branco,pos,4)
        fonte = pygame.font.Font(None,20)
        texto = fonte.render(nome,True,branco)
        tela.blit(texto,(pos[0]+15,pos[1]-10))

def junta_pontos():
    superficie_desenho.fill((0, 0, 0, 0))
    if len(pontos)>=2:
        for i in range(len(pontos)-1):
            pygame.draw.line(superficie_desenho,branco,(pontos[i]),(pontos[i+1]),2)

def soma():
    soma_total = sum([sum(valores) for valores in estrelas.values()])
    fonte = pygame.font.Font(None, 20)
    texto = fonte.render("Soma: " + str(soma_total), True, branco)
    tela.blit(texto, (1, 60))


running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif  evento.type == pygame.KEYDOWN and evento.key== pygame.K_ESCAPE:
            running = False
            
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F10:
            tela.fill(branco)
            tela.blit(fundo, (-100,0))
            limpaTela()
            apagar_arquivo("histórico.txt")
            
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F11:
            print("histórico não disponível")
        elif evento.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space","Nome da estrela: ")
            
            if item == "":
                item = "Desconhecido"+str(pos)
               
            estrelas[item] = pos
            print(estrelas)

            arquivo = open("Histórico.txt","a")
            arquivo.write(item+"\n")
            arquivo.close
    
    tela.fill(branco)
    tela.blit(fundo,(-100,0))
    desenha_estrela()
    soma()
    junta_pontos()
    superficie_desenho = pygame.Surface(tamanho)
    pontos = list(estrelas.values())
    texto1 = fonte.render("precione ESQ para fechar o programa: ",True,branco)
    texto2 = fonte.render("precione F10 para apagar os pontos: ",True,branco)
    texto3 = fonte.render("precione F11 para carregar o histórico: ",True,branco)
    tela.blit(texto1,(1,10))
    tela.blit(texto2,(1,28))
    tela.blit(texto3,(1,45))

    pygame.display.update()
pygame.quit()
