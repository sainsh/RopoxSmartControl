import pygame
import sys
import time

width= 800
height = 600
size = [width,height]
bg = [0,0,0]

screen = pygame.display.set_mode(size)

def main():
        pygame.init()
        clock = pygame.time.Clock()
        fps=60
        

        tl_button = pygame.Rect(width/4*1-width/5/2, height/4, width/5, height/5)
        tm_button = pygame.Rect(width/4*2-width/5/2, height/4, width/5, height/5)
        tr_button = pygame.Rect(width/4*3-width/5/2, height/4, width/5, height/5)
        bl_button = pygame.Rect(width/4*1-width/5/2, height/2, width/5, height/5)
        bm_button = pygame.Rect(width/4*2-width/5/2, height/2, width/5, height/5)
        br_button = pygame.Rect(width/4*3-width/5/2, height/2, width/5, height/5)

        pygame.display.set_caption('ROPOX')
        
        pygame.draw.rect(screen, [255, 0, 0], tl_button)
        pygame.draw.rect(screen, [255, 0, 0], tm_button)
        pygame.draw.rect(screen, [255, 0, 0], tr_button)
        pygame.draw.rect(screen, [255, 0, 0], bl_button)
        pygame.draw.rect(screen, [255, 0, 0], bm_button)
        pygame.draw.rect(screen, [255, 0, 0], br_button)# draw buttons
        message_display("PROFIL",width/4*1,height/3+10)
        message_display("BORD",width/4*2,height/3+10)
        message_display("SKAB",width/4*3,height/3+10)
        message_display("LÅS",width/4*1,height/1.75+15)
        message_display("OVN",width/4*2,height/1.75+15)
        message_display("INDSTILLINGER",width/4*3,height/1.75+15)

        message_display("ROPOX",width/2,height/10)
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
                        print('button was pressed at {0}'.format(mouse_pos))
            

            screen.fill(bg)

            

            #pygame.display.update()
            clock.tick(fps)

        pygame.quit()
        sys.exit

def text_objects(text, font):
    textSurface = font.render(text, True, pygame.Color(255,255,255))
    return textSurface, textSurface.get_rect()

def message_display(text,x,y):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y)
    screen.blit(TextSurf, TextRect)
    #pygame.display.update()


if __name__ == '__main__':
    main()