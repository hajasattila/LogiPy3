import pygame  # játék funckiók
import os  # Operációs rendszer parancsai, elérési utvonalakhoz fog kelleni
import math  # különböző számításokat, sebzéseket, stb ez fog megoldani
import random  # Random elemek generálása(kövi órán meteorok)

# Értékek inicializálása
pygame.font.init()
pygame.mixer.init()

# Konstansok - > nem változnak az értékek, csak nagybetűvel vannak írva
WIDTH, HEIGHT = 900, 550
# Ablak mérete
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

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

# CSAK METEOR TULAJDONSÁGOK
METEOR_WIDTH, METEOR_HEIGHT = 50, 50
METERO_VEL = 2
METEOR1_DIR = random.randint(0, 359)
METEOR2_DIR = random.randint(0, 359)
METEOR3_DIR = random.randint(0, 359)

METEOR1_X_VEL = math.cos(METEOR1_DIR) * METERO_VEL
METEOR1_Y_VEL = math.sin(METEOR1_DIR) * METERO_VEL

METEOR2_X_VEL = math.cos(METEOR2_DIR) * METERO_VEL
METEOR2_Y_VEL = math.sin(METEOR2_DIR) * METERO_VEL

METEOR3_X_VEL = math.cos(METEOR3_DIR) * METERO_VEL
METEOR3_Y_VEL = math.sin(METEOR3_DIR) * METERO_VEL

METEOR_IMG = pygame.image.load(os.path.join('Assets', 'meteor.png'))

METEOR1 = pygame.transform.rotate(pygame.transform.scale(
    METEOR_IMG, (METEOR_WIDTH, METEOR_HEIGHT)), 90)
METEOR2 = pygame.transform.rotate(pygame.transform.scale(
    METEOR_IMG, (METEOR_WIDTH, METEOR_HEIGHT)), 90)
METEOR3 = pygame.transform.rotate(pygame.transform.scale(
    METEOR_IMG, (METEOR_WIDTH, METEOR_HEIGHT)), 90)

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

#Ide fogjuk eltárolni az adatokat.
PATH = "eredmenyek.txt"
