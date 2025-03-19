import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
screen.fill((255,255,0))
cl = pygame.time.Clock()
x=250
y=250
q=True

while q:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            q=False
    pygame.draw.circle(screen, (255,0,0),(x,y),(25))
    press=pygame.key.get_pressed()
    if press[pygame.K_UP]:
        if y > 25:
            y -=20
    if press[pygame.K_DOWN]:
        if y < 475:
            y+=20
    if press[pygame.K_LEFT]:
        if x > 25:
            x-=20
    if press[pygame.K_RIGHT]:
        if x < 475:
            x+=20
    pygame.display.flip()
    cl.tick(60)