import pygame
import datetime


pygame.init()
fon = pygame.display.set_mode((1400, 1050))
clock = pygame.time.Clock()


imgCL = pygame.image.load('clock.png')
imgL = pygame.image.load('leftarm.png')
imgR = pygame.image.load('rightarm.png')


centerL = (700, 525)  
centerR = (700, 525) 


def rotate_arm(image, angle, center):
    rotated_image = pygame.transform.rotate(image, -angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect.topleft

imgR,b = rotate_arm(imgR,50,centerR)
imgL,c = rotate_arm(imgL,5,centerL)

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    

    now = datetime.datetime.now()
    MIN = now.minute
    SEC = now.second


    sec_angle = 6 * SEC 
    min_angle = 6 * MIN 


    rotated_L, posL = rotate_arm(imgL, sec_angle, centerL)
    rotated_R, posR = rotate_arm(imgR, min_angle, centerR)


    fon.fill((255, 255, 255))
    fon.blit(imgCL, (0, 0))  
    fon.blit(rotated_L, posL)  
    fon.blit(rotated_R, posR) 

    pygame.display.flip()
    clock.tick(60)  

pygame.quit()