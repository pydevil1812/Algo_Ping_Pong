import pygame
 
WIDTH = 800
HEIGHT = 600
BALL_COLOR = (0, 255, 0)
LEFT_COLOR = (255, 0, 0)
BLACK = (0, 0, 0)
 
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ping Pong')
clock = pygame.time.Clock()
running = True
x = 0
y = 0
speed = 7
speedx = speed
speedy = speed
yleft = 250
yright = 250
 
score_left = 0
score_right = -3
 
while running:
    window.fill((43, 79, 52))
    clock.tick(60)
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    x += speedx
    y += speedy
    ball = pygame.draw.circle(window, BALL_COLOR, (x, y), 25)
 
    keys = pygame.key.get_pressed()
    
    left = pygame.draw.rect(window, LEFT_COLOR, (30, yleft, 20, 100))
    right = pygame.draw.rect(window, LEFT_COLOR, (WIDTH-30, yright, 20, 100))
 
    if keys[pygame.K_w] and left.top > 0:
        yleft -= speed
    if keys[pygame.K_UP] and right.top > 0:
        yright -= speed
 
    if keys[pygame.K_s] and left.bottom < HEIGHT:
        yleft += speed
    if keys[pygame.K_DOWN] and right.bottom < HEIGHT:
        yright += speed
 
    if left.colliderect(ball):
        speedx = speed
    if right.colliderect(ball):
        speedx = -speed
 
    if ball.right >= WIDTH:
        speedx = -speed
        score_left += 1
 
    if ball.left <= 0:
        speedx = speed
        score_right += 1
 
    if ball.bottom >=HEIGHT:
        speedy = -speed    
    
    if ball.top <= 0:
        speedy = speed
 
    font = pygame.font.Font(None, 50)
    text = font.render(str(score_left), 1, BLACK)
    window.blit(text, (250, 10))
    text = font.render(str(score_right),1, BLACK)
    window.blit(text, (520, 10))
 
    pygame.display.update()
pygame.quit()
