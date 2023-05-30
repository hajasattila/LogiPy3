import pygame
import random
import sys

pygame.init()
myVector = pygame.math.Vector2
HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60
FramePerSec = pygame.time.Clock()
displaySurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect(center=(10, 420))
        self.pos = myVector((10, 385))
        self.vel = myVector(0, 0)
        self.acc = myVector(0, 0)
        self.jumping = False
    def move(self):
        self.acc = myVector(0, 0.5)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[pygame.K_RIGHT]:
            self.acc.x = ACC
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

    def update(self):
        hits = pygame.sprite.spritecollide(P1, platforms, False)
        if hits and P1.vel.y > 0:
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0
            self.jumping = False
        self.rect.midbottom = self.pos
    def jump(self):
        hits = pygame.sprite.spritecollide(P1, platforms, False)
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -15
    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50, 100), 12))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect(center=(random.randint(0, WIDTH - 10), random.randint(0, HEIGHT - 30)))

def platform_generator():
    while len(platforms) < 7:
        width = random.randrange(50, 100)
        p = Platform()
        c = True
        while c:
            p = Platform()
            p.rect.center = (random.randrange(0, WIDTH - width), random.randrange(-50, 0))
            c = check(p, platforms)
        platforms.add(p)
        all_sprites.add(p)


def check(platform, groupies):
    if pygame.sprite.spritecollideany(platform, groupies):
        return True
    else:
        for new_plat in groupies:
            if new_plat == platform:
                continue
            if (abs(platform.rect.top - new_plat.rect.bottom) < 50)\
                    and (abs(platform.rect.bottom - new_plat.rect.top) < 50):
                return True


PT1 = Platform()
PT1.surf = pygame.Surface((WIDTH, 20))
PT1.surf.fill((255, 0, 0))
PT1.rect = PT1.surf.get_rect(center=(WIDTH / 2, HEIGHT - 10))
P1 = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

platforms = pygame.sprite.Group()
platforms.add(PT1)

for x in range(random.randint(5, 6)):
    C = True
    pl = Platform()
    while C:
        pl = Platform()
        C = check(pl, platforms)
    platforms.add(pl)
    all_sprites.add(pl)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                P1.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                P1.cancel_jump()
    displaySurface.fill((0, 0, 0))

    if P1.rect.top <= HEIGHT / 3:
        P1.pos.y += abs(P1.vel.y)
        for plat in platforms:
            plat.rect.y += abs(P1.vel.y)
            if plat.rect.top >= HEIGHT:
                plat.kill()

    P1.move()
    P1.update()
    platform_generator()
    for entity in all_sprites:
        displaySurface.blit(entity.surf, entity.rect)

    pygame.display.update()
    FramePerSec.tick(FPS)
