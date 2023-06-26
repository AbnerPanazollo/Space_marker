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
pygame.display.set_caption("Space Marker")
pygame.display.set_icon(nave)
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
fonte = pygame.font.Font(None, 20)

def limpaTela():
    os.system("cls")
def apagar_arquivo(nome_arquivo):
    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)
        print(f"Arquivo '{nome_arquivo}' apagado com sucesso!")
    else:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
def desenha_estrela():
    for nome,pos in estrelas.items():
        pygame.draw.circle(tela,branco,pos,4)
        fonte = pygame.font.Font(None,20)
        texto = fonte.render(nome,True,branco)
        tela.blit(texto,(pos[0]+15,pos[1]-10))

running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif  evento.type == pygame.KEYDOWN and evento.key== pygame.K_ESCAPE:
            running = False
            
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F10:
            limpaTela()
            apagar_arquivo("histórico.txt")
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F11:
            pass
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

    texto1 = fonte.render("precione ESQ para fechar o programa: ",True,branco)
    texto2 = fonte.render("precione F10 para apagar os pontos: ",True,branco)
    texto3 = fonte.render("precione F11 para carregar o histórico: ",True,branco)
    tela.blit(texto1,(1,10))
    tela.blit(texto2,(1,28))
    tela.blit(texto3,(1,45))
    

    pygame.display.update()
pygame.quit()
