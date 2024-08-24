import pygame

pygame.init()


size = (600, 380)
win = pygame.display.set_mode(size)
framework = pygame.image.load("images/background.png")

win.blit(source=framework, dest=(0, 0))


state = True

while state:
    win.blit(source=framework, dest=(0, 0))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
   

