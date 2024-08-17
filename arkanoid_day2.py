import pygame
pygame.init()
from myClass import Picture

''' color '''
back_color = (200, 255, 255)


''' variables '''
game_over = False
racket_x = 200
racket_y = 300

start_x = 5
start_y = 5

move_right = False
move_left = False

speed_x = 2
speed_y = 2


''' scense object '''
window = pygame.display.set_mode((500,500))
window.fill(back_color)
clock = pygame.time.Clock()


''' game objects '''
ball = Picture(filename='ball.png', x=160, y=200, width=50, height=50)
platform = Picture(filename='platform.png', x=racket_x, y=racket_y, width=100,  height=30)

''' loop monster objects '''
monsters = list()

count = 9

for j in range(3): 
    y = start_y + (55 * j) 
    x = start_x + (27.5 * j) 

    for i in range (count):
        d = Picture('enemy.png', x, y, 50, 50) 
        monsters.append(d) 
        x = x + 55 
    count = count - 1


''' game loop '''
while not game_over:
    ball.fill()
    platform.fill()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: 
                move_right = True 

            if event.key == pygame.K_LEFT:
                move_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False 

            if event.key == pygame.K_LEFT:
                move_left = False

    if move_right == True:
        platform.rect.x += 3

    if move_left == True:
        platform.rect.x -= 3

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.colliderect(platform.rect):
        speed_y *= -1
    if ball.rect.y < 0:
        speed_y *= -1
    if ball.rect.x > 450 or ball.rect.x < 0:
        speed_x *= -1
            

    ball.draw()
    platform.draw()

    for m in monsters:
        m.draw()
    
    pygame.display.update()
    clock.tick(40)