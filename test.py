import sys
import pygame
from IPWebCam import *

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((600,600))

ipcam = IPWEBCAM('192.168.2.94:8080', width=600, height=600) # thats the server address shown on the IP webcam, don't add 'http://' the class adds it

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_f:
                ipcam.swap_camera()
            if event.key == pygame.K_b:
                ipcam.swap_camera('off')
            if event.key == pygame.K_o:
                ipcam.overlay("on")
            if event.key == pygame.K_p:
                ipcam.overlay()
            if event.key == pygame.K_l:
                ipcam.led("on")
            if event.key == pygame.K_m:
                ipcam.led()
    screen.blit(ipcam.get_pygame_image(),(0,0))
    pygame.display.flip()
    clock.tick(0)
