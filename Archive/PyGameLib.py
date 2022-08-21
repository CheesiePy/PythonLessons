# from pygame import mixer

# #start mixer

# mixer.init()

# # load the sound acoording the relative path
# mysound = mixer.Sound("Sound1.mp3")

# # play the sound

# mixer.Sound.play(mysound)

import pygame

pygame.init()

dis = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Game!")

blue = (0, 0, 255)
red = (255, 0, 0)




gameOver = False



while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    pygame.draw.rect(dis,blue,[290,150,10,10])
    pygame.display.update()

pygame.quit()
quit()
