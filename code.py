from pygame import *
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))

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
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect > 5:
           self.speed -= self.speed 
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect > 5:
            self.rect -= self.speed

craket1 = Player('racket.png',30,270,50,150,3)
#craket2 = Player('racket.png',)

while game:
    display.update()
    clock.tick(60)
    for i in event.get():
        if e.type == QUIT:
            game = False
