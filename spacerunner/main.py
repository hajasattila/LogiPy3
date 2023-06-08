# Könytárak használata - Libraryk
import pygame  # játék funckiók
import konstans as kon
import controller as cont
# Ablak címe
pygame.display.set_caption("SpaceRunner")


def main():
    red = pygame.Rect(700, 200, kon.SSW, kon.SSH)
    yellow = pygame.Rect(100, 200, kon.SSW, kon.SSH)

    meteor_1 = pygame.Rect(480, 240, kon.METEOR_WIDTH, kon.METEOR_HEIGHT)
    meteor_2 = pygame.Rect(480, 240, kon.METEOR_WIDTH, kon.METEOR_HEIGHT)
    meteor_3 = pygame.Rect(480, 240, kon.METEOR_WIDTH, kon.METEOR_HEIGHT)

    redBullets, yellowBullets = [], []
    redHealth, yellowHealth = 6, 6
    clock = pygame.time.Clock()
    run = True
    while run != False:
        clock.tick(kon.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            # Ha megfelelő gombot nyomunk le, akkor kilövi a lövedéket a megfelelő hajó
            # Feltétel, hogy ne legyen elfogyva a töltényünk.
            # Mindig oda rajzolja, amelyik oldalról előjjük
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellowBullets) < kon.MAXBULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.height, yellow.y + yellow.width // 2, 10, 5)
                    yellowBullets.append(bullet)
                    kon.BULLETFIRESOUND.play()
                if event.key == pygame.K_RCTRL and len(redBullets) < kon.MAXBULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + red.width // 2, 10, 5)
                    redBullets.append(bullet)
                    kon.BULLETFIRESOUND.play()
            # Ha betalál egy bullet, akkor hang effekt, és menjen le az élet
            if event.type == kon.REDHIT:
                redHealth -= 1
                kon.BULLETHITSOUND.play()
            if event.type == kon.YELLOWHIT:
                yellowHealth -= 1
                kon.BULLETHITSOUND.play()
            winnerText = ""
            if redHealth <= 0:
                winnerText = "Srága nyert"
            if yellowHealth <= 0:
                winnerText = "Piros nyert"
            if winnerText != "":
                cont.drawWinner(winnerText)
                pygame.quit()
        keysPressed = pygame.key.get_pressed()
        cont.yellowControl(keysPressed, yellow)
        cont.redControl(keysPressed, red)

        cont.handleBullets(yellowBullets, redBullets, yellow,
                           red, meteor_1, meteor_2, meteor_3)

        cont.meteorController(meteor_1, meteor_2, meteor_3)

        cont.drawWindow(red, yellow, redBullets,
                        yellowBullets, redHealth, yellowHealth, meteor_1, meteor_2, meteor_3)
    main()


if __name__ == "__main__":
    main()
