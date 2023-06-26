import pygame
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

running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space","Nome da estrela: ")
            print(item)
            if item == "":
                item = "Desconhecido"+str(pos)
            estrelas[item] = pos
            print(estrelas)
            arquivo = open("Histórico de estrelas","a")
            arquivo.write(item+"\n")
            arquivo.close

    tela.fill(branco)
    tela.blit(fundo,(-100,0))

    

    pygame.display.update()
pygame.quit()
