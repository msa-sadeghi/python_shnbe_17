import pygame
pygame.init()
import random
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
clock = pygame.time.Clock()
color = (100, 200, 100)

f = pygame.font.SysFont("arial", 22)
score = 0
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            r= random.randint(0, 255)
            g= random.randint(0, 255)
            b= random.randint(0, 255)
            color = (r,g,b)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color = "black"
    # screen.fill((100, 200, 100))
    screen.fill(color)
    score_text = f.render(f"Score {score}", True, "white")
    screen.blit(score_text, (10, 10))
    pygame.display.update()
    clock.tick(FPS)