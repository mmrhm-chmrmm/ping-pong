import pygame



WINDOW_SIZE =(1200, 900)
WIN_W, WIN_H = WINDOW_SIZE
FPS = 60


WHITE = (255, 255, 255)



class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, step_size, image_filename):
        super().__init__()
        self.image = pygame.image.load(image_filename)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = pygame.rect.Rect(x, y, width, height)
        self.speed = step_size

    def reset(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def __init__(self, x, y, width, height, step_size, image_filename, firesound_filename):
        super().__init__(x, y, width, height, step_size, image_filename)
        self.keys = {
            'UP': None,
            'DOWN': None
        }


    def set_control_keys(self, key_up, key_down):
        self.keys = {
            'UP': key_up,
            'DOWN': key_down
        }
    
    def update(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[self.keys['UP']] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[self.keys['DOWN']] and self.rect.y < WIN_H - self.rect.height:
            self.rect.y += self.speed

    
class Ball(GameSprite): 
    def __init__(self, x, y, width, height, step_size, image_filename):
        super().__init__(x, y, width, height, step_size, image_filename)
        self.speed_x = step_size
        self.speed_y = step_size

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y >= WIN_H - self.rect.height or self.rect.y <= 0:
            self.speed_y = -self.speed_y







main_window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('ПИНГ-ПОНГ')
background_image = pygame.image.load('background.jpg')
background_image = pygame.transform.scale(background_image, WINDOW_SIZE)
clock = pygame.time.Clock()


player_1 = Player(80, 350, 20, 200, 5, 'rocket.png', None)
player_2 = Player(WIN_W - 100, 350, 20, 200, 5, 'rocket.png', None)
player_1.set_control_keys(pygame.K_UP, pygame.K_DOWN)
player_2.set_control_keys(pygame.K_w, pygame.K_s)   
ball = Ball(600, 450, 25, 25, 3, 'ball.png')






is_finished = False
is_running = True
while is_running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            is_running = False
    
    if not is_finished:
        player_1.update()
        player_2.update()
        ball.update()
        if pygame.sprite.spritecollideany(ball, [player_1, player_2]):
            ball.speed_x = -ball.speed_x
    main_window.blit(background_image, (0, 0))
    player_1.reset(main_window)
    player_2.reset(main_window)
    ball.reset(main_window)
    pygame.display.update()
    clock.tick(FPS)


