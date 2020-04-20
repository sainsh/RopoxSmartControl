import pygame
import sys
import time
from rasp_paste import goUp
from rasp_paste import goDown

width = 800
height = 600
size = [width, height]
bg = [0, 0, 0]

clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode(size)


def main():
    pygame.init()

    main_screen()

    pygame.quit()
    sys.exit


def text_objects(text, font):
    textSurface = font.render(text, True, pygame.Color(255, 255, 255))
    return textSurface, textSurface.get_rect()


def message_display(text, x, y):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    screen.blit(TextSurf, TextRect)
    # pygame.display.update()


def button(x, y, width, height, color):

    button = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, button)
    return button


def main_screen():
    # create and display buttons
    tl_button = button(width/4*1-width/5/2, height/4,
                       width/5, height/5, [255, 0, 0])
    tm_button = button(width/4*2-width/5/2, height/4,
                       width/5, height/5, [255, 0, 0])
    tr_button = button(width/4*3-width/5/2, height/4,
                       width/5, height/5, [255, 0, 0])
    bl_button = button(width/4*1-width/5/2, height/2,
                       width/5, height/5, [255, 0, 0])
    bm_button = button(width/4*2-width/5/2, height/2,
                       width/5, height/5, [255, 0, 0])
    br_button = button(width/4*3-width/5/2, height/2,
                       width/5, height/5, [255, 0, 0])

    pygame.display.set_caption('ROPOX')

    message_display("PROFIL", width/4*1, height/3+10)
    message_display("BORD", width/4*2, height/3+10)
    message_display("SKAB", width/4*3, height/3+10)
    message_display("LÅS", width/4*1, height/1.75+15)
    message_display("OVN", width/4*2, height/1.75+15)
    message_display("INDSTILLINGER", width/4*3, height/1.75+15)

    message_display("ROPOX", width/2, height/10)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

                if tl_button.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print(
                        'TopLeft button was pressed at {0}'.format(mouse_pos))
                elif tm_button.collidepoint(mouse_pos):
                    print('TopMid button was pressed at {0}'.format(mouse_pos))
                    bord_screen()
                    break

                elif tr_button.collidepoint(mouse_pos):
                    print(
                        'TopRight button was pressed at {0}'.format(mouse_pos))
                elif bl_button.collidepoint(mouse_pos):
                    print(
                        'BottomLeft button was pressed at {0}'.format(mouse_pos))
                elif bm_button.collidepoint(mouse_pos):
                    print(
                        'BottomMid button was pressed at {0}'.format(mouse_pos))
                elif br_button.collidepoint(mouse_pos):
                    print(
                        'BottomRight button was pressed at {0}'.format(mouse_pos))

        screen.fill(bg)

        # pygame.display.update()
        clock.tick(fps)


def bord_screen():
    pygame.display.update()
    print("bord screen")

    tl_button = button(width/4*1-width/5/2, height/4,
                       width/5, height/5, [255, 0, 0])
    tm_button = button(width/4*2-width/5/2, height/4,
                       width/5, height/5, [255, 0, 0])
    tr_button = button(width/4*3-width/5/2, height/4,
                       width/5, height/5, [255, 0, 0])
    bl_button = button(width/4*1-width/5/2, height/2,
                       width/5, height/5, [255, 0, 0])
    bm_button = button(width/4*2-width/5/2, height/2,
                       width/5, height/5, [255, 0, 0])
    br_button = button(width/4*3-width/5/2, height/2,
                       width/5, height/5, [255, 0, 0])

    message_display("↑OP", width/4*1, height/3+10)
    message_display("Højde", width/4*2, height/3+10)
    message_display("Lås", width/4*3, height/3+10)
    message_display("↓NED", width/4*1, height/1.75+15)
    message_display("Profil", width/4*2, height/1.75+15)
    message_display("Tilbage", width/4*3, height/1.75+15)

    message_display("Bord", width/2, height/10)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

                if tl_button.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print(
                        'TopLeft button was pressed at {0}'.format(mouse_pos))
                    goUp();
                elif tm_button.collidepoint(mouse_pos):
                    print('TopMid button was pressed at {0}'.format(mouse_pos))
                elif tr_button.collidepoint(mouse_pos):
                    print(
                        'TopRight button was pressed at {0}'.format(mouse_pos))
                elif bl_button.collidepoint(mouse_pos):
                    print(
                        'BottomLeft button was pressed at {0}'.format(mouse_pos))
                    goDown()
                elif bm_button.collidepoint(mouse_pos):
                    print(
                        'BottomMid button was pressed at {0}'.format(mouse_pos))
                elif br_button.collidepoint(mouse_pos):
                    print(
                        'BottomRight button was pressed at {0}'.format(mouse_pos))
        clock.tick(fps)


if __name__ == '__main__':
    main()
