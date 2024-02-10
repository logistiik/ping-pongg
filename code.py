from pygame import *
win_width = 700
win_height = 500
window = display.setmode((win_width, win_height))

FPS  = 60
game = True

class GameSprite(sprite.Sprite):
    def init(self, player_image,player_x,player_y,size_x,size_y,player_speed):
        sprite.Sprite.init(self)
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
        
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x>5:
            self.rect.x-=self.speed
        if keys_pressed[K_RIGHT] and self.rect.x<695:
            self.rect.x+=self.speed
    def update(self):
        keys = key.get_pressed()
        if keys[K_w]

while game:
 for i in event.get():
     if i.type == QUIT:
         game = False

