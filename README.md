This is a simple script that helps in accessing the image from the Android App
IP Webcam and to be able to display it in pygame


# Requirements
1. **opencv 2**
2. **numpy**
3. **pygame**

# Usage

```python
import sys
import pygame
from IPWebCam import *

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((176,144))

ipcam = IPWEBCAM('192.168.1.103:8080') # thats the server address shown on the IP webcam, don't add 'http://' the class adds it

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      pygame.quit()
      sys.exit()
  screen.blit(ipcam.get_pygame_image(),(0,0))
  pygame.display.flip()
  clock.tick(0)
```

# TODO
Add support for Image resolution
