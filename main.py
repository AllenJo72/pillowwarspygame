import pygame
import random
import math
import sys

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1600, 900), 0, 32)
height = pygame.display.Info().current_h
width = pygame.display.Info().current_w


background = pygame.image.load("assets/background.jpg")

pygame.display.set_caption("Pillow Wars")
icon = pygame.image.load("assets/pillow.png")
pygame.display.set_icon(icon)


playerImg = pygame.image.load("assets/pillow2.png")
playerX = 800
playerY = 800
playerX_change = 0


enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('assets/enemy2.png'))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)


star_field_slow = []
star_field_medium = []
star_field_fast = []


WHITE = (255, 255, 255)
LIGHTGREY = (192, 192, 192)
DARKGREY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BOOTSCREEN = (0,0,128)


for slow_stars in range(50):
    star_loc_x = random.randrange(0, width)
    star_loc_y = random.randrange(0, height)
    star_field_slow.append([star_loc_x, star_loc_y])

for medium_stars in range(35):
    star_loc_x = random.randrange(0, width)
    star_loc_y = random.randrange(0, height)
    star_field_medium.append([star_loc_x, star_loc_y])

for fast_stars in range(15):
    star_loc_x = random.randrange(0, width)
    star_loc_y = random.randrange(0, height)
    star_field_fast.append([star_loc_x, star_loc_y])



bulletImg = pygame.image.load('assets/cotton2.png')
bulletX = 0
bulletY = 800
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.SysFont('rockwell', 32)

textX = 10
testY = 10

# Game Over text
over_font = pygame.font.SysFont('rockwell', 64)



def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (650, 400))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "shoot"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.hypot(enemyX - bulletX, enemyY - bulletY)
    if distance < 27:
        return True
    else:
        return False
font1 = pygame.font.SysFont('candara', 45)
font2 = pygame.font.SysFont('consolas', 130)
font3 = pygame.font.SysFont('consolas', 70)
font4= pygame.font.SysFont('bookmanoldstyle', 20)
font5 = pygame.font.SysFont('rockwell', 30)
font6 = pygame.font.SysFont('rockwell', 15)

start_game_button = pygame.image.load('assets/Srtopt.png')
start_game_buttonX = 660
start_game_buttonY = 400

option_button = pygame.image.load('assets/Srtopt.png').convert_alpha()
option_buttonX = 660
option_buttonY = 500


def start_game_button_set(x, y):
    screen.blit(start_game_button, (x, y))

def option_button_set(x, y):
    screen.blit(option_button, (x, y))

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False
def main_menu():
    global click
    start_ticks = pygame.time.get_ticks()
    while True:


        screen.fill((WHITE))
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(660, 400, 312, 75)
        if seconds > 1:
            pygame.draw.rect(screen, (30, 144, 255), button_1)
            if button_1.collidepoint((mx, my)):
                if click:
                    game()
        button_2 = pygame.Rect(660, 500, 312, 75)
        if seconds > 1:
            pygame.draw.rect(screen, (30, 144, 255), button_2)
            if button_2.collidepoint((mx, my)):
                if click:
                    options_screen()


        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        for star in star_field_slow:
            star[1] += 1
            if star[1] > height:
                star[0] = random.randrange(0, width)
                star[1] = random.randrange(-20, -5)
            pygame.draw.circle(screen, DARKGREY, star, 3)

        for star in star_field_medium:
            star[1] += 4
            if star[1] > height:
                star[0] = random.randrange(0, width)
                star[1] = random.randrange(-20, -5)
            pygame.draw.circle(screen, YELLOW, star, 2)

        for star in star_field_fast:
            star[1] += 8
            if star[1] > height:
                star[0] = random.randrange(0, width)
                star[1] = random.randrange(-20, -5)
            pygame.draw.circle(screen, MAGENTA, star, 1)

        draw_text('Pillow Wars', font2, (30, 144, 255), screen, 430, 70)
        start_game_button_set(start_game_buttonX, start_game_buttonY)
        draw_text('Start', font3, (255, 255, 255), screen, 715, 410)
        option_button_set(option_buttonX, option_buttonY)
        draw_text('Options', font3, (255, 255, 255), screen, 685, 505)
        pygame.display.update()
        clock.tick(60)


def options_screen():
    # Nothing in option screen yet. Trying to add audio settings in here.
    running = True
    while running:
        screen.fill(WHITE)
        mx, my = pygame.mouse.get_pos()
        draw_text('Options', font2, (30, 144, 255), screen, 600, 70)

        back_button = pygame.Rect(50, 800, 150, 50)
        if back_button.collidepoint((mx, my)):
            if click:
                main_menu()
        pygame.draw.rect(screen, (30, 144, 255), back_button)
        draw_text('Back', font1, (255, 255, 255), screen, 80, 805)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        for star in star_field_slow:
            star[1] += 1
            if star[1] > height:
                star[0] = random.randrange(0, width)
                star[1] = random.randrange(-20, -5)
            pygame.draw.circle(screen, DARKGREY, star, 3)

        for star in star_field_medium:
            star[1] += 4
            if star[1] > height:
                star[0] = random.randrange(0, width)
                star[1] = random.randrange(-20, -5)
            pygame.draw.circle(screen, YELLOW, star, 2)

        for star in star_field_fast:
            star[1] += 8
            if star[1] > height:
                star[0] = random.randrange(0, width)
                star[1] = random.randrange(-20, -5)
            pygame.draw.circle(screen, MAGENTA, star, 1)
        pygame.display.flip()
        clock.tick(60)


def game():
    global playerX_change
    start_ticks = pygame.time.get_ticks()
    global playerX, playerY, bulletY, bulletX, bullet_state, score_value
    running = True
    while running:


        screen.fill((0, 0, 0))
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state is "ready":

                        bulletX = playerX
                        fire_bullet(playerX, bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        playerX += playerX_change

        if playerX <= 0:
            playerX = 0
        elif playerX >= 1500:
            playerX = 1500


        for i in range(num_of_enemies):

            #Game Over
            if enemyY[i] > 700:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                if seconds > 2:
                    main_menu()

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 4
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 1500:
                enemyX_change[i] = -4
                enemyY[i] += enemyY_change[i]

            # Collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:

                bulletY = 800
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 735)
                enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)

        if bulletY <= 0:
            bulletY = 800
            bullet_state = "ready"

        if bullet_state == "shoot":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change


        player(playerX, playerY)
        show_score(textX, testY)
        pygame.display.update()
        clock.tick(60)
main_menu()
