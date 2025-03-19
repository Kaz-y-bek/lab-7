import pygame 
pygame.init()
pygame.mixer.init()
songs = ['9 Грамм feat.Miyagi, Эндшпиль.mp3','Kairat Nurtas- Ақ келін.mp3','Sadraddin- Taxi.mp3','Sadradd3in- Tun.mp','Turar- Иіс.mp3','Fire Man   Miyagi   Эндшпиль.mp3']

i = 0
pygame.mixer.music.load(songs[i%len(songs)])


screen = pygame.display.set_mode((450,400))
pygame.display.set_caption("My music")
fonq = pygame.image.load('fon.png')

q = True
while q:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            q = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                i += 1
                i = i%len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()


            elif event.key == pygame.K_LEFT:
                i -= 1
                i = i%len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()


            elif event.key == pygame.K_UP:
                if i == 0:
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.unpause()

            
            elif event.key == pygame.K_DOWN:
                pygame.mixer.music.pause()
    screen.blit(fonq, (0, 0))
    pygame.display.flip()
pygame.quit()



    