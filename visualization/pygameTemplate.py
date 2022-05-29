import sys, pygame
pygame.init()

size = width, height = 800, 600
black = 0, 0, 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen = pygame.display.set_mode(size)
    screen.fill(black)
    pygame.draw.circle(screen, (255, 0, 0), (100, 100), 20)
    pygame.display.flip()
