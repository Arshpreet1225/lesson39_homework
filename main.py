import pygame
import random
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader Project - Part 2")
bg_image = pygame.image.load("background.png")
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
score = 0
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 40)) 
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 20
        self.speed = 5
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30)) 
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - 30)
        self.rect.y = random.randint(50, SCREEN_HEIGHT - 200)
all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(7):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemy_group.add(enemy)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    collisions = pygame.sprite.spritecollide(player, enemy_group, True)
    for hit in collisions:
        score += 1 
        print(f"Collision detected! Current Score: {score}")
    screen.blit(bg_image, (0, 0))
    all_sprites.draw(screen)
    font = pygame.font.SysFont("Arial", 30)
    score_surface = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_surface, (10, 10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()