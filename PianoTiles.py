
import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
gray = (100,169,169)
yellow = (255,255,0)

display_width = 600
display_height = 950

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Piano Tiles")

font = pygame.font.SysFont(None, 50)
end_font = pygame.font.SysFont(None, 30)
wait_font = pygame.font.SysFont(None, 90)
clock = pygame.time.Clock()

def GameLoop():

    def GameOver():
        screen_text = wait_font.render("Wait 4 sec...", True, green)
        gameDisplay.blit(screen_text, (120, 450))
        screen_text = wait_font.render("Game Over!", True, red)
        gameDisplay.blit(screen_text, (120, 380))
        screen_text = font.render("Your score is: " + str(wynik), True, red)
        gameDisplay.blit(screen_text, (120, 520))
        pygame.display.update()

    gameExit = False

    start = 0
    FPS = 60
    wynik = 0

    yl = (random.randint(-1000, -300))
    yl_change = 0
    trafienie_yl = 0

    ym = (random.randint(-1000, -300))
    ym_change = 0
    trafienie_ym = 0

    yr = (random.randint(-1000, -300))
    yr_change = 0
    trafienie_yr = 0

    kolor_l = black
    kolor_m = black
    kolor_r = black

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    start += 1
                if event.key == pygame.K_LEFT:
                    if start >= 2:
                        if trafienie_yl >= 1:
                            los_yl = (random.randint(-1000, -300))
                            yl = los_yl
                            trafienie_yl = 0
                            wynik += 1
                        else:
                            pygame.draw.rect(gameDisplay, gray, [0, 700, 200, 10])
                            pygame.display.update()
                            GameOver()
                            pygame.time.delay(4000)
                            GameLoop()
                if event.key == pygame.K_DOWN:
                    if start >= 2:
                        if trafienie_ym >= 1:
                            los_ym = (random.randint(-1100, -300))
                            ym = los_ym
                            trafienie_ym = 0
                            wynik += 1
                        else:
                            pygame.draw.rect(gameDisplay, gray, [200, 700, 200, 10])
                            pygame.display.update()
                            GameOver()
                            pygame.time.delay(4000)
                            GameLoop()
                if event.key == pygame.K_RIGHT:
                    if start >= 2:
                        if trafienie_yr >= 1:
                            los_yr = (random.randint(-1200, -300))
                            yr = los_yr
                            trafienie_yr = 0
                            wynik += 1
                        else:
                            pygame.draw.rect(gameDisplay, gray, [400, 700, 200, 10])
                            pygame.display.update()
                            GameOver()
                            pygame.time.delay(4000)
                            GameLoop()

        if start == 1:
            start += 1
            yl_change += 10
            ym_change += 10
            yr_change += 10

        if wynik == 10:
            FPS = 70
        if wynik == 20:
            FPS = 80
        if wynik == 30:
            FPS = 90
        if wynik == 40:
            FPS = 110
        if wynik == 50:
            FPS = 120
        if wynik == 60:
            FPS = 130
        if wynik == 80:
            FPS = 140
        if wynik == 100:
            FPS = 150
        if wynik == 120:
            FPS = 160

        yl += yl_change
        ym += ym_change
        yr += yr_change

        if yl > 450:
            trafienie_yl += 1
        if yl > 705:
            pygame.draw.rect(gameDisplay, gray, [0, 710, 200, 250])
            pygame.display.update()
            GameOver()
            pygame.time.delay(4000)
            GameLoop()

        if ym > 450:
            trafienie_ym += 1
        if ym > 705:
            pygame.draw.rect(gameDisplay, gray, [200, 710, 200, 250])
            pygame.display.update()
            GameOver()
            pygame.time.delay(4000)
            GameLoop()

        if yr > 450:
            trafienie_yr += 1
        if yr > 705:
            pygame.draw.rect(gameDisplay, gray, [400, 710, 200, 250])
            pygame.display.update()
            GameOver()
            pygame.time.delay(4000)
            GameLoop()


        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, kolor_l, [0, yl, 200, 250])
        pygame.draw.rect(gameDisplay, kolor_m, [200, ym, 200, 250])
        pygame.draw.rect(gameDisplay, kolor_r, [400, yr, 200, 250])
        pygame.draw.rect(gameDisplay, red, [0, 700, 950, 10])
        pygame.draw.rect(gameDisplay, red, [0, 0, 950, 50])
        screen_text = font.render("Score: " + str(wynik), True, black)
        gameDisplay.blit(screen_text, (10, 8))
        screen_text = end_font.render("Controls: left, down, right ARROW", True, black)
        gameDisplay.blit(screen_text, (260, 5))
        screen_text = end_font.render("UpArrow to start the game", True, black)
        gameDisplay.blit(screen_text, (300, 25))
        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()
    quit()

GameLoop()