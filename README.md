# Pygame Animation
This lib allows you use your gif animation in pygame


## Installation
#### Step 1: Download Lib
if you have git installed, use:
`git clone https://github.com/maxtaran2010/PygameAnimation.git`
if you don't, download the zip file and unzip it.

#### Step 2: Install requirements
run this command in the project folder:
  ` python3 -m pip install -r requirements.txt `

## Overview
> You can see the example in example.py file

### Basic animation
```py
from pygameAnimations import Animation as Anim
import pygame

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
anim = Anim('<path>', screen, <scale>, delay=<delay-between-updates>)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((0, 0, 0))
    anim.draw(<x>, <y>)
    pygame.display.flip()


```
Replace \<path\> with your path to gif file, \<scale\> with your scale coeficient, \<delay-between-updates\> with your delay between updates of animation, \<x\> and \<y\> with position of drawing the gif on the screen
 
  ### Pause/Unpause
  to pause animation, use:
  ```py
  anim.playing = Flase
  ```
  to unpause:
  ```py
  anim.playing = True
  ```
  
  ### Set frame
  to set the frame, use:
  ```py
  anim.frame = <frame>
  ```
  replace \<frame\> with the frame you need
  
  ### Flip image
  to set the static flip coeficient, use:
  ```py
  anim.flip = <x>, <y>
  ```
  replace \<x\> and \<y\> with flip coeficient by x and y
  
  ## Notes
  * When you stop animation, it automaticly returning to the first frame
  * This is `Beta` Version!
  * Lib supports only `.gif` and `.png` formats.
  
