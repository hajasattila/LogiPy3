# Könytárak használata - Libraryk
import pygame  # játék funckiók
import os  # Operációs rendszer parancsai, elérési utvonalakhoz fog kelleni
import math  # különböző számításokat, sebzéseket, stb ez fog megoldani
import random  # Random elemek generálása(kövi órán meteorok)

# TODO: lehetett volna a konstansokat kiszervezni másik .py fileba

# Értékek inicializálása
pygame.font.init()
pygame.mixer.init()
# Konstansok - > nem változnak az értékek, csak nagybetűvel vannak írva
WIDTH, HEIGHT = 900, 550
# Ablak mérete
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# Ablak címe
pygame.display.set_caption("SpaceRunner")
# Színek RGB(red,green,blue)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
# Szegély
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
# Hangok
BULLETHITSOUND = pygame.mixer.Sound(os.path.join("Assets", "explosion.wav"))
BULLETFIRESOUND = pygame.mixer.Sound(os.path.join("Assets", "laser.wav"))
#FONTOK, KIIRÁSOK
HEALTFONT = pygame.font.SysFont("arial", 40)
WINNERFONT = pygame.font.SysFont("arial", 100)
# Érték változók pl: FPS, sebesség...
FPS = 60
VEL = 5
BULLETVEL = 7
MAXBULLETS = 3
SSW = 80
SSH = 60
# Jelmezek
# Háttér
SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join("Assets", "space.png")), (WIDTH, HEIGHT))
# Esemény
YELLOWHIT = pygame.USEREVENT + 1
REDHIT = pygame.USEREVENT + 2
# Kép, és megjelenítés
YELLOWSSIMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_yellow.png"))
YELLOWSPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOWSSIMAGE, (SSW, SSH)), 90)

REDSSIMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_red.png"))
REDSPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(REDSSIMAGE, (SSW, SSH)), 270)

# Sárga kontroller irányok alapján mondjuk meg, hogy éppen mi növekedjen, vagy csökkenjen
def yellowControl(keysPressed, yellow):
    if keysPressed[pygame.K_a] and yellow.x - VEL > -15:  # balra
        yellow.x -= VEL
    if keysPressed[pygame.K_d] and yellow.x + VEL + yellow.height - 35 < BORDER.x:  # jobbra
        yellow.x += VEL
    if keysPressed[pygame.K_w] and yellow.y - VEL > -10:  # fel
        yellow.y -= VEL
    if keysPressed[pygame.K_s] and yellow.y + VEL + yellow.width < HEIGHT:  # le
        yellow.y += VEL

# Piros kontroller irányok alapján mondjuk meg, hogy éppen mi növekedjen, vagy csökkenjen
def redControl(keysPressed, red):
    if keysPressed[pygame.K_LEFT] and red.x - VEL + 15 > BORDER.x + BORDER.width:  # balra
        red.x -= VEL
    if keysPressed[pygame.K_RIGHT] and red.x + VEL + red.height - 35 < WIDTH:  # jobbra
        red.x += VEL
    if keysPressed[pygame.K_UP] and red.y - VEL > -10:  # fel
        red.y -= VEL
    if keysPressed[pygame.K_DOWN] and red.y + VEL + red.width < HEIGHT:  # le
        red.y += VEL


def drawWindow(red, yellow, redBullets, yellowBullets, redHealth, yellowHealth):
    #Ablak építse meg a SPace konstant ami a háttér lesz, é 0,0 pozícióból induljon el
    WINDOW.blit(SPACE, (0, 0))
    pygame.draw.rect(WINDOW, BLACK, BORDER)
    redHealthText = HEALTFONT.render(f"Élet:{redHealth}", True, WHITE)
    yellowHealthText = HEALTFONT.render(f"Élet:{yellowHealth}", True, WHITE)
    WINDOW.blit(YELLOWSPACESHIP, (yellow.x, yellow.y))
    WINDOW.blit(REDSPACESHIP, (red.x, red.y))
    WINDOW.blit(redHealthText, (WIDTH-redHealthText.get_width() - 10, 10))
    WINDOW.blit(yellowHealthText, (10, 10))
    for bullet in redBullets:
        pygame.draw.rect(WINDOW, RED, bullet)
    for bullet in yellowBullets:
        pygame.draw.rect(WINDOW, YELLOW, bullet)
    pygame.display.update()


def handleBullets(yellowBullets, redBullets, yellow, red):
    #Megvizsgáljuk a sárga töltényeket
    for bullet in yellowBullets:
        #Növeljük a pozícit, így jobbra fog menni a töltény, a BULETVEL értékével
        bullet.x += BULLETVEL
        #Ha eltaláljuk a piros entitást(szereplőt), akkor tünjön el
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(REDHIT))
            yellowBullets.remove(bullet)
            #Vagy, ha kimegy a pálya szélére
        elif bullet.x > WIDTH:
            yellowBullets.remove(bullet)
    #Ugyan az a logika mind a kettőnél csak egyik jobbra, másik balra lő
    for bullet in redBullets:
        bullet.x -= BULLETVEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOWHIT))
            redBullets.remove(bullet)
        elif bullet.x < 0:
            redBullets.remove(bullet)



def drawWinner(text):
    pass


def main():
    red = pygame.Rect(700, 200, SSW, SSH)
    yellow = pygame.Rect(100, 200, SSW, SSH)
    redBullets = []
    yellowBullets = []
    redHealth = 10
    yellowHealth = 10
    clock = pygame.time.Clock()
    run = True
    while run != False:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
        keysPressed = pygame.key.get_pressed()
        yellowControl(keysPressed, yellow)
        redControl(keysPressed, red)
        drawWindow(red, yellow, redBullets, yellowBullets, redHealth, yellowHealth)
    main()


if __name__ == "__main__":
    main()
