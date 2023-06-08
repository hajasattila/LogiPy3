import pygame  # játék funckiók
import konstans as kon
from datetime import datetime
# Sárga kontroller irányok alapján mondjuk meg, hogy éppen mi növekedjen, vagy csökkenjen


def yellowControl(keysPressed, yellow):
    if keysPressed[pygame.K_a] and yellow.x - kon.VEL > -15:  # balra
        yellow.x -= kon.VEL
    if keysPressed[pygame.K_d] and yellow.x + kon.VEL + yellow.height - 35 < kon.BORDER.x:  # jobbra
        yellow.x += kon.VEL
    if keysPressed[pygame.K_w] and yellow.y - kon.VEL > -10:  # fel
        yellow.y -= kon.VEL
    if keysPressed[pygame.K_s] and yellow.y + kon.VEL + yellow.width < kon.HEIGHT:  # le
        yellow.y += kon.VEL

# Piros kontroller irányok alapján mondjuk meg, hogy éppen mi növekedjen, vagy csökkenjen


def redControl(keysPressed, red):
    if keysPressed[pygame.K_LEFT] and red.x - kon.VEL + 15 > kon.BORDER.x + kon.BORDER.width:  # balra
        red.x -= kon.VEL
    if keysPressed[pygame.K_RIGHT] and red.x + kon.VEL + red.height - 35 < kon.WIDTH:  # jobbra
        red.x += kon.VEL
    if keysPressed[pygame.K_UP] and red.y - kon.VEL > -10:  # fel
        red.y -= kon.VEL
    if keysPressed[pygame.K_DOWN] and red.y + kon.VEL + red.width < kon.HEIGHT:  # le
        red.y += kon.VEL

# TODO: MEGOLDANI, HOGY A LÖVÉSEK NE MENJENEK ÁT AZ ASZTEROIDÁKON


def drawWindow(red, yellow, redBullets, yellowBullets, redHealth, yellowHealth, meteor_1, meteor_2, meteor_3):
    # Ablak építse meg a SPace konstant ami a háttér lesz, é 0,0 pozícióból induljon el
    kon.WINDOW.blit(kon.SPACE, (0, 0))
    pygame.draw.rect(kon.WINDOW, kon.BLACK, kon.BORDER)

    redHealthText = kon.HEALTFONT.render(f"Élet:{redHealth}", True, kon.WHITE)
    yellowHealthText = kon.HEALTFONT.render(
        f"Élet:{yellowHealth}", True, kon.WHITE)

    kon.WINDOW.blit(kon.YELLOWSPACESHIP, (yellow.x, yellow.y))
    kon.WINDOW.blit(kon.REDSPACESHIP, (red.x, red.y))
    kon.WINDOW.blit(redHealthText, (kon.WIDTH -
                    redHealthText.get_width() - 10, 10))
    kon.WINDOW.blit(yellowHealthText, (10, 10))

    # Meteorok megint
    kon.WINDOW.blit(kon.METEOR1, (meteor_1.x, meteor_1.y))
    kon.WINDOW.blit(kon.METEOR2, (meteor_2.x, meteor_2.y))
    kon.WINDOW.blit(kon.METEOR3, (meteor_3.x, meteor_3.y))

    for bullet in redBullets:
        pygame.draw.rect(kon.WINDOW, kon.RED, bullet)

    for bullet in yellowBullets:
        pygame.draw.rect(kon.WINDOW, kon.YELLOW, bullet)
    pygame.display.update()


def handleBullets(yellowBullets, redBullets, yellow, red, meteor_1, meteor_2, meteor_3):
    # Megvizsgáljuk a sárga töltényeket
    for bullet in yellowBullets:
        # Növeljük a pozícit, így jobbra fog menni a töltény, a BULETVEL értékével
        bullet.x += kon.BULLETVEL
        # Ha eltaláljuk a piros entitást(szereplőt), akkor tünjön el
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(kon.REDHIT))
            yellowBullets.remove(bullet)
            # Vagy, ha kimegy a pálya szélére
        elif bullet.x > kon.WIDTH:
            yellowBullets.remove(bullet)

    # Ugyan az a logika mind a kettőnél csak egyik jobbra, másik balra lő
    for bullet in redBullets:
        bullet.x -= kon.BULLETVEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(kon.YELLOWHIT))
            redBullets.remove(bullet)
        elif bullet.x < 0:
            redBullets.remove(bullet)

    # Sárga meteorok érintése
    if yellow.colliderect(meteor_1):
        meteor_1.x = 480
        meteor_1.y = 240
        pygame.event.post(pygame.event.Event(kon.YELLOWHIT))
    if yellow.colliderect(meteor_2):
        meteor_2.x = 480
        meteor_2.y = 240
        pygame.event.post(pygame.event.Event(kon.YELLOWHIT))
    if yellow.colliderect(meteor_3):
        meteor_3.x = 480
        meteor_3.y = 240
        pygame.event.post(pygame.event.Event(kon.YELLOWHIT))

    # Piros meteor esetek
    if red.colliderect(meteor_1):
        meteor_1.x = 480
        meteor_1.y = 240
        pygame.event.post(pygame.event.Event(kon.REDHIT))
    if red.colliderect(meteor_2):
        meteor_2.x = 480
        meteor_2.y = 240
        pygame.event.post(pygame.event.Event(kon.REDHIT))
    if red.colliderect(meteor_3):
        meteor_3.x = 480
        meteor_3.y = 240
        pygame.event.post(pygame.event.Event(kon.REDHIT))


def drawWinner(text):
    drawText = kon.WINNERFONT.render(text, True, kon.WHITE)
    kon.WINDOW.blit(drawText, (kon.WIDTH / 2 - drawText.get_width() /
                               2, kon.HEIGHT / 2 - drawText.get_height() / 2))
    pygame.display.update()

    # Próbákozik mindig hozzáadni egy új sort
    try:
        with open(kon.PATH, "a+", encoding="utf8") as file:
            # Kiírjuk egy fileba a nyerési időpontját. Dátummal ellátva, a tizedes mp levágva a végéről
            print(
                f"{text}, ekkor: { datetime.now().strftime('%Y-%m-%d %H:%M:%S') }", file=file)
    # Ha nem létezik, akkor létrehozza
    except FileNotFoundError:
        with open(kon.PATH, "w+", encoding="utf8") as file:
            print(
                f"{text}, ekkor: { datetime.now().strftime('%Y-%m-%d %H:%M:%S') }", file=file)
    pygame.time.delay(5000)


def meteorController(meteor1, meteor2, meteor3):
    # Meteorok mozgatása
    meteor1.x += kon.METEOR1_X_VEL
    meteor1.y += kon.METEOR1_Y_VEL
    meteor2.x += kon.METEOR2_X_VEL
    meteor2.y += kon.METEOR2_Y_VEL
    meteor3.x += kon.METEOR3_X_VEL
    meteor3.y += kon.METEOR3_Y_VEL
    # Se felül, se alul nem tudunk kimenni, sem jobb, sem bal oldalt a meteorokkal.
    # METEOR1
    # x tengelyen ha kimegy, balra, akkor menjen jobbra
    if meteor1.x > 899:
        meteor1.x = 1
        # ha jobbra, akkor balra
    if meteor1.x < 1:
        meteor1.x = 899
        # ha fent megy ki, akkor menjen vissza alulra
    if meteor1.y > 549:
        meteor1.y = 1
        # ha alul, menjen fentre
    if meteor1.y < 1:
        meteor1.y = 549

    # METEOR2
    if meteor2.x > 899:
        meteor2.x = 1
    if meteor2.x < 1:
        meteor2.x = 899
    if meteor2.y > 549:
        meteor2.y = 1
    if meteor2.y < 1:
        meteor2.y = 549

    # METEOR3
    if meteor3.x > 899:
        meteor3.x = 1
    if meteor3.x < 1:
        meteor3.x = 899
    if meteor3.y > 549:
        meteor3.y = 1
    if meteor3.y < 1:
        meteor3.y = 549