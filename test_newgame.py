import pygame
import os
import random

WIDTH = 480
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("shooter kitty")
clock = pygame.time.Clock()
#set up assets

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "cat.png")).convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2 
        self.rect.bottom = HEIGHT -10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        
        keystate = pygame.key.get_pressed()
        
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
            
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

            
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image = pygame.image.load(os.path.join(img_folder, "heart.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 10)
        
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-80, -40)
            self.speedy = random.randrange(1, 3)
            
class Bullet(pygame.sprite.Sprite):
     def __init__(self, x, y):
         pygame.sprite.Sprite.__init__(self)
         self.image = pygame.Surface((10, 20))
         self.image.fill(GREEN)
         self.rect = self.image.get_rect()
         self.rect.bottom = y
         self.rect.centerx = x
         self.speedy = -10
         
     def update(self):
         self.rect.y += self.speedy
         if self.rect.bottom < 0:
             self.kill()
             
    #  def shoot(self):
    #      bullet = Bullet(self.rect.centerx, self.rect.top)
    #      all_sprites.add(bullet)
    #      bullets.add(bullet)

background = pygame.image.load(os.path.join(img_folder, 'sky.jpeg')).convert()
background_rect = background.get_rect()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets =  pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
    

     
# screen.fill((0,0,0))
running = True
while running:
    
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
            
     
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    
    all_sprites.update()
   
    
    
    # hits = pygame.sprite.spritecollide(player, mobs, False)
    # if hits:
    #     running = False
        
  
    
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit() 
              
            
    
  
    
   
            

            
