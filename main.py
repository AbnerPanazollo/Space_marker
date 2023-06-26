import pygame

pygame.init()
tamanho = (800,563)
tela = pygame.display.set_mode(tamanho)
nave = pygame.image.load("space.png")
fundo = pygame.image.load("bg.jpg")
branco = (255,255,255)
pygame.display.set_caption("Space Marker")
pygame.display.set_icon(nave)

running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
    tela.fill(branco)
    tela.blit(fundo,(-100,0))
    pygame.display.update()
pygame.quit()
