#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import pygame
import sys
import time
import trainSubprocess
from pygame.locals import *
import os
from queue import *


if(os.name != "nt"):
    import GPIOController as table
from threading import Thread

width = 800
height = 480
size = [width, height]
bg = [0, 0, 0]
btn_width = 180
btn_height = 100
buttons = [None] * 6

ON_POSIX = 'posix' in sys.builtin_module_names

clock = pygame.time.Clock()
fps = 60

screen = ""
pygame.mouse.set_visible = False

currentScreen = "main"

def main():
    global screen
    screen = pygame.display.set_mode(size)
    pygame.init()
    myfont = pygame.font.SysFont("freesansbold", 30)
    #Dette bruges til at køre Sopare
    process = subprocess.Popen(('./sopare.py -l'), shell = True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, close_fds=ON_POSIX, cwd="../sopare")
    q = Queue() #Maybe little q in queue
    t = threading.Thread(target=enqueue_output, args=(process.stdout, q))
    t.daemon = True
    t.start()

    while True:
        #using our enqueue_output thread to find out if sopare has sent anything
        try:  line = q.get_nowait() # or q.get(timeout=.1)
        except Empty:
            pass #do nothing
        else: # got a line from sopare
            nextline = line
            if process.poll() is not None:
                break
            #decoding from bytes to string
            currentline = nextline.decode()
            #This is where our if/elif statements will control the GPIO pins when a specific word is recognized
            if("ropox" in currentline):
                table.goUp(5) #Needs all logic and the command tree

        #optimized layoutcontrol
        if(currentScreen == "main"):
            sixButtonLayout(["PROFIL", "BORD", "SKAB", u"LÅS", "OVN", "INDSTILLINGER"], myfont) # 123Ovn kunne måske ændres til træning
        elif(currentScreen == "table"):
            sixButtonLayout(["OP", u"HØJDE", u"LÅS", "NED", "PROFIL", "TILBAGE"], myfont)
        elif(currentScreen == "settings"):
            sixButtonLayout(["Sprog", u"Træn", u"Følsomhed", "Udtræk Data", "Ydligere?", "TILBAGE"], myfont)
        elif(currentScreen == "training"):
            sixButtonLayout(["Ropox", u"Bord", u"Hæv", "Sænk/Ned", "Stop", "TILBAGE"], myfont)         

            #123 Her kunne laves endnu et elif(): med nogle navne til knapper i træningsscreen, op, ned, ropox, bord tilbage
            #Currentscreen kunne blive døbt training

            # display headline
        pygame.display.set_caption('ROPOX')
        text("ROPOX", myfont, (width/2, height/10))
        pygame.display.flip()
        #managing clicks on buttons
        keepGoing = sixButtonEventHandler()
        if not keepGoing:
            break
        screen.fill(bg)
        clock.tick(fps)
        
    pygame.quit()
    if(os.name != "nt"):
        table.cleanUp()
    sys.exit
       
#Queue that sends through results from Sopare
def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()

#This method can handle clicks on our 6 button layout screen. Called once every iteration in main loop
def sixButtonEventHandler():
    global currentScreen
    #Running through all events this iteration
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

                                                     #### TODO: CHECK WORDS IN ALL trainSubprocess.Train() ####
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

                if buttons[0].collidepoint(mouse_pos):
                    if(currentScreen == "main"):
                        print("Write functionality here")
                        
                    elif(currentScreen == "table"):
                        table.goUp(5)

                    elif(currentScreen == "settings"):
                        print("Sprog")

                    elif(currentScreen == "training"):
                        #Will start training of the word Ropox
                        trainSubprocess.train("Ropox")

                    
                elif buttons[1].collidepoint(mouse_pos):
                    if(currentScreen == "main"):
                        currentScreen = "table"

                    elif(currentScreen == "table"):
                        print("Write functionality here")

                    elif(currentScreen == "settings"):
                        currentScreen = "training"

                    elif(currentScreen == "training"):
                        #Will start training of the word Bord
                        trainSubprocess.train("bord")
                    
                elif buttons[2].collidepoint(mouse_pos):
                    if(currentScreen == "main"):
                        print("Write functionality here")
                        
                    elif(currentScreen == "table"):
                        print("Write functionality here")

                    elif(currentScreen == "training"):
                        #Will start training of the word Hæv
                        trainSubprocess.train("hæv")

                elif buttons[3].collidepoint(mouse_pos):
                    if(currentScreen == "main"):
                        print("Write functionality here")
                        
                    elif(currentScreen == "table"):
                        table.goDown(5)

                    elif(currentScreen == "training"):
                        #Will start training of the word Sænk/Ned
                        trainSubprocess.train("ned")             
                elif buttons[4].collidepoint(mouse_pos):
                    if(currentScreen == "main"):
                        print("Write functionality here")
                        #123 her sætter man ind at currentscreen = training så navigerer pygame til den skærm
                        #Der skal også tilføjes elif til alle disse "listeners" med elif(currentscreen == "training")
                    
                    elif(currentScreen == "table"):
                        print("Write functionality here")
                        #123 Der skal også tilføjes elif til alle disse "listeners" med elif(currentscreen == "training")
                        #Den når der klikkes på training -> op eksempelvis skal vores subprocessTraiining unktionalitet køres.
                        #Det kan nok gøres noglelunde på samme måde som vores subprocessRun køres i mainloopet
                    elif(currentScreen == "training"):
                        #Will start training of the word Stop
                        trainSubprocess.train("stop") 

                    
                elif buttons[5].collidepoint(mouse_pos):
                    if(currentScreen == "main"):
                        currentScreen == "settings"
                        
                    elif(currentScreen == "table"):
                        currentScreen = "main"

                    elif(currentScreen == "settings"):
                        currentScreen = "main"    

                    elif(currentScreen == "training"):
                        currentScreen = "settings" 
                    
            if(event.type == pygame.KEYDOWN):
                if(event.key == K_ESCAPE):
                    return False
    return True

#creating button
def button(x, y, width, height, color):

    button = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, button)
    return button

#Creating six buttons in layout :
#[0][1][2]
#[3][4][5]
def sixButtonLayout(names, myfont):
    # create and display buttons
        buttons[0] = button(width/4*1-btn_width/2, height/4,
                           btn_width, btn_height, [255, 0, 0])
        buttons[1] = button(width/4*2-btn_width/2, height/4,
                           btn_width, btn_height, [255, 0, 0])
        buttons[2] = button(width/4*3-btn_width/2, height/4,
                           btn_width, btn_height, [255, 0, 0])
        buttons[3] = button(width/4*1-btn_width/2, height/2,
                           btn_width, btn_height, [255, 0, 0])
        buttons[4] = button(width/4*2-btn_width/2, height/2,
                           btn_width, btn_height, [255, 0, 0])
        buttons[5] = button(width/4*3-btn_width/2, height/2,
                           btn_width, btn_height, [255, 0, 0])

        # display text for buttons
        text(names[0], myfont, buttons[0].center)
        text(names[1], myfont, buttons[1].center)
        text(names[2], myfont, buttons[2].center)
        text(names[3], myfont, buttons[3].center)
        text(names[4], myfont, buttons[4].center)
        text(names[5], myfont, buttons[5].center)


def text(txt, myfont, location):
    text_to_display = myfont.render(txt, 1, (255, 255, 255))
    placement = (location[0]-text_to_display.get_rect().width/2,
                 location[1]-text_to_display.get_rect().height/2)
    screen.blit(text_to_display, placement)




if __name__ == '__main__':
    main()
    
