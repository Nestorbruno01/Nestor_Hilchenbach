# importing required library
import pygame
import random

# constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1200
BACKGROUND_COLOR = (0,100,0) # RGB

class Gorilla:
    def __init__(self):
        img = pygame.image.load("Gorilla.png")
        self.img = pygame.transform.scale(img, (200,200))
        self.img2 = pygame.transform.flip(img,True,False)
        self.img2 = pygame.transform.scale(self.img2,(200,200))
        # init position
        self.pos_x = 0
        self.pos_y = 300
        self.moving_forward = True

    def tint(self):
        # option: tint your image if you want
        self.img.fill((0, 255, 100, 100), special_flags=pygame.BLEND_ADD)
        pass

    def animate(self):
        if self.pos_x < banana.pos_x:
            self.moving_forward = True
            self.pos_x += 3
            if self.pos_y < banana.pos_y:
                self.pos_y += 3
            elif self.pos_y > banana.pos_y:
                self.pos_y -= 3
            else:
                if abs (self.pos_x - banana.pos_x) <= 20:
                    self.moving_forward = False
        else:
            self.moving_forward = False
            self.pos_x += -3
            if self.pos_y < banana.pos_y:
                self.pos_y += 3
            elif self.pos_y > banana.pos_y:
                self.pos_y -= 3
            else:
                if abs (self.pos_x - banana.pos_x) <= 20:
                    self.moving_forward = True

    def draw(self):
        if self.moving_forward:
            screen.blit(self.img, (self.pos_x, self.pos_y))
        else:
            screen.blit(self.img2, (self.pos_x, self.pos_y))

class Banana:
    def __init__(self):
        img2 = pygame.image.load("Banana.png")
        self.img2 = pygame.transform.scale(img2, (50,50))
        self.pos_x = 1100
        self.pos_y = 350

    def animate(self):
        if abs(self.pos_x - gorilla.pos_x) < 20 and abs(self.pos_y - gorilla.pos_y) < 20:
            self.pos_x = random.randrange(0, 800)
            self.pos_y = random.randrange(0, 800)

    def draw(self):
        screen.blit(self.img2, (self.pos_x, self.pos_y))

# activate the pygame library
pygame.init()

# create the display surface object
# of specific dimension.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set the pygame window name
pygame.display.set_caption('Hungry Gorilla')

# Create one dino object at a start location
gorilla = Gorilla()
banana = Banana()

# Init the clock
clock = pygame.time.Clock()

flag = True
while flag:
    # ticking the clock
    clock.tick(60)

    # update dino's position
    gorilla.animate()
    banana.animate()

    # paint the screen with background color
    screen.fill(BACKGROUND_COLOR)
    # Using blit to copy image to screen at a specific location
    gorilla.draw()
    banana.draw()
    # refresh the display
    pygame.display.flip()

    # code you need to end pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

pygame.quit()
exit(0)