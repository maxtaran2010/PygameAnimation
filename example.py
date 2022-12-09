from pygameAnimations import Animation as Anim
import pygame

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
anim = Anim('example.gif', screen, 2, delay=10)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((0, 0, 0))
    anim.draw(50, 50)
    pygame.display.flip()
