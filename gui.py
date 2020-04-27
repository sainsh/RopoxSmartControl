import pygame
import sys
import time
from pygame.locals import *
import rasp_paste as rp

width = 800
height = 600
size = [width, height]
bg = [0, 0, 0]
btn_width = 180
btn_height = 120


clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode(size)


def main():
    pygame.init()
    myfont = pygame.font.SysFont("freesansbold", 30)
    while True:
        next = main_screen(myfont)
        if(next == "bord"):
            next = bord_screen(myfont)
        elif(next == "tilbage"):
            next = main_screen(myfont)
        elif(next == False):
            break
    pygame.quit()
    sys.exit


def button(x, y, width, height, color):

    button = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, button)
    return button


def main_screen(myfont):

    while True:
        # create and display buttons
        tl_button = button(width/4*1-btn_width/2, height/4,
                           btn_width, btn_height, [255, 0, 0])
        tm_button = button(width/4*2-btn_width/2, height/4,
                           btn_width, btn_height, [255, 0, 0])
        tr_button = button(width/4*3-btn_width/2, height/4,
                           btn_width, btn_height, [255, 0, 0])
        bl_button = button(width/4*1-btn_width/2, height/2,
                           btn_width, btn_height, [255, 0, 0])
        bm_button = button(width/4*2-btn_width/2, height/2,
                           btn_width, btn_height, [255, 0, 0])
        br_button = button(width/4*3-btn_width/2, height/2,
                           btn_width, btn_height, [255, 0, 0])

        # display text for buttons
        text("PROFIL", myfont, tl_button.center)
        text("BORD", myfont, tm_button.center)
        text("SKAB", myfont, tr_button.center)
        text("LÅS", myfont, bl_button.center)
        text("OVN", myfont, bm_button.center)
        text("INDSTILLINGER", myfont, br_button.center)

        # display headline
        pygame.display.set_caption('ROPOX')
        text("ROPOX", myfont, (width/2, height/10))

        pygame.display.flip()
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
                    return "bord"

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

        clock.tick(fps)


def bord_screen(myfont):
    h = 0
    pygame.display.flip()
    up = False
    down = False
    counter = 0
    while True:
        # create and display buttons
        tl_button = button(width/4*1-btn_width/2, height/4,
                           btn_width, btn_height, [255, 0, 0])
        tm_button = button(width/4*2-btn_width/2, height/4,
                           btn_width, btn_height, [255, 0, 0])
        tr_button = button(width/4*3-btn_width/2, height/4,
                           btn_width, btn_height, [255, 0, 0])
        bl_button = button(width/4*1-btn_width/2, height/2,
                           btn_width, btn_height, [255, 0, 0])
        bm_button = button(width/4*2-btn_width/2, height/2,
                           btn_width, btn_height, [255, 0, 0])
        br_button = button(width/4*3-btn_width/2, height/2,
                           btn_width, btn_height, [255, 0, 0])
        # display text for buttons
        text("OP", myfont, tl_button.center)
        text("HØJDE", myfont, tm_button.center)
        text("LÅS", myfont, tr_button.center)
        text("NED", myfont, bl_button.center)
        text("PROFIL", myfont, bm_button.center)
        text("TILBAGE", myfont, br_button.center)
        text(str(h), myfont, (tm_button.center[0], tm_button.center[1]+30))

        # display headline
        pygame.display.set_caption('ROPOX')
        text("BORD", myfont, (width/2, height/10))

        pygame.display.flip()
        
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
                    rp.goUp()
                    up=True
                    down=False
                elif tm_button.collidepoint(mouse_pos):
                    print('TopMid button was pressed at {0}'.format(mouse_pos))
                elif tr_button.collidepoint(mouse_pos):
                    print(
                        'TopRight button was pressed at {0}'.format(mouse_pos))
                elif bl_button.collidepoint(mouse_pos):
                    print(
                        'BottomLeft button was pressed at {0}'.format(mouse_pos))
                    rp.goDown()
                    down=True
                    up=False
                elif bm_button.collidepoint(mouse_pos):
                    print(
                        'BottomMid button was pressed at {0}'.format(mouse_pos))
                elif br_button.collidepoint(mouse_pos):
                    print(
                        'BottomRight button was pressed at {0}'.format(mouse_pos))
                    return "tilbage"
        screen.fill(bg)
        if(up):
            h += 1
        elif(down):
            h -= 1
        clock.tick(fps)
        counter +=1
        if(counter % 20 == 0):
            up=False
            down=False


def text(txt, myfont, location):
    text_to_display = myfont.render(txt, 1, (255, 255, 255))
    placement = (location[0]-text_to_display.get_rect().width/2,
                 location[1]-text_to_display.get_rect().height/2)
    screen.blit(text_to_display, placement)


if __name__ == '__main__':
    main()
