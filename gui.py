#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import pygame
import sys
import time
from pygame.locals import *
import os
import Queue
import signal
import io

#JSON imports (Localization implementation)
import json


with io.open('./settings.json') as settingsFile:
    settings = json.load(settingsFile)
lang = settings['lang']
with io.open('./Localization/{}.json'.format(lang), encoding='utf8' ) as jsonFile:
    strings = json.load(jsonFile)
def words(word):
    return strings["text"][word]

def picture(word):
    return strings["pictures"][word]


if(os.name != "nt"):
    import GPIOController as table
from threading import Thread
width = 800
height = 480
size = [width, height]
bg = [0, 0, 0]
btn_width = width/4
btn_height = height/3
stopBtn_width = 800
stopBtn_height = 400
buttons = [None] * 6
action = ""

ON_POSIX = 'posix' in sys.builtin_module_names

clock = pygame.time.Clock()
fps = 60

screen = ""
pygame.mouse.set_visible = False

listening = False
tablelistening = False

currentScreen = "main"

def main():
    global screen
    global currentScreen
    global listening
    global tablelistening
    global height
    global width
    screen = pygame.display.set_mode(size)
    pygame.init()
    #width = pygame.display.Info().current_w
    #height = pygame.display.Info().current_h
    #pygame.mouse.set_visible(False)
    myfont = pygame.font.SysFont("freesansbold", 30)
    #Used for running sopare
    process = subprocess.Popen(('./sopare.py -l'), shell = True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=0, close_fds=ON_POSIX, cwd="../../sopare")
    q = Queue.Queue() #Maybe little q in queue
    t = Thread(target=enqueue_output, args=(process.stdout, q))
    t.daemon = True
    t.start()

    try:
        while True:
            #using our enqueue_output thread to find out if sopare has sent anything
            try:  line = q.get_nowait() # or q.get(timeout=.1)
                
            except Queue.Empty:
                pass #do nothing
            else: # got a line from sopare
                nextline = line
                print(list(q.queue))
                if process.poll() is not None:
                    break
                #decoding from bytes to string
                currentline = nextline.decode()
                print("should be working???")
                #This is where our if/elif statements will control the GPIO pins when a specific word is recognized
                if("result:stop" in currentline):
                    table.stopTable()
                    listening = False
                    tablelistening = False
                    currentScreen = "main"
                if("result:ropox" in currentline):
                    listening = True
                    tablelistening = False
                    currentScreen = "listening"
                    waitThread = Thread(target = wait, )
                    waitThread.daemon = False
                    waitThread.start
                    #Lytter skærm
                if listening:
                    if("result:table" in currentline):
                        tablelistening = True
                        listening = False
                if tablelistening:
                    if("result:up" in currentline):
                        table.goUp(5)
                        tablelistening = False
                        action = words("respondsRaise")
                        currentScreen = "stop"
                        # STOP button
                    elif("result:down" in currentline):
                        table.goDown(5)
                        tablelistening = False
                        action = words("respondsLower")
                        currentScreen = "stop"
                        # STOP button
            #optimized layoutcontrol
            if(currentScreen == "main"):
                sixButtonLayout([words("profile"), words("table"), words("cupboard"), 
                words("lock"), words("cupboard"), words("settings")], myfont)
            elif(currentScreen == "table"):
                sixButtonLayout([picture("raiseArrow"), words("height"), words("lock"), 
                picture("lowerArrow"), words("profile"), words("back")], myfont)
            elif(currentScreen == "settings"):
                sixButtonLayout([words("language"), words("train"), "...", 
                words("exportData"), "...", words("back")], myfont)
            elif(currentScreen == "training"):
                sixButtonLayout(["Ropox", words("table"), words("raise"), 
                words("lower"), words("stop"), words("back")], myfont)
            elif(currentScreen == "stop"):
                stopButtonLayout(words("stop"), myfont, action)
            elif(currentScreen == "listening"):
                if(listening):
                    listeningLayout(words("respondsListen"))
                elif(tablelistening):
                    listeningLayout(words("respondsTable"))

                #123 Her kunne laves endnu et elif(): med nogle navne til knapper i træningsscreen, op, ned, ropox, bord tilbage
                #Currentscreen kunne blive døbt training

            pygame.display.set_caption('ROPOX')
            if(currentScreen != "stop"):   # display headline
                text("ROPOX", myfont, (width/2, height/10))
            pygame.display.flip()
            #managing clicks on buttons
            if(currentScreen == "stop"):
                keepGoing = stopButtonEventHandler()
            else:
                keepGoing = sixButtonEventHandler()
            if not keepGoing:
                break
            screen.fill(bg)
            clock.tick(fps)
    except Exception as e:
        if(os.name != "nt"):
            #os.kill(os.getpid(process.pid), signal.SIGTERM)
            table.stopTable()
            table.cleanUp()
        print(e)

    if(os.name != "nt"):    
        #os.kill(os.getpid(process.pid), signal.SIGTERM)
        table.stopTable()
        table.cleanUp()
    pygame.quit()
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
                       pass
                    elif(currentScreen == "stop"):
                        #STOP
                        table.stopTable()

                    
                elif buttons[1].collidepoint(mouse_pos):
                    if(currentScreen == "main"):
                        currentScreen = "table"

                    elif(currentScreen == "table"):
                        print("Write functionality here")

                    elif(currentScreen == "settings"):
                        currentScreen = "training"

                    elif(currentScreen == "training"):
                        #Will start training of the word Table
                        pass
                    
                elif buttons[2].collidepoint(mouse_pos):
                    if(currentScreen == "main"):
                        print("Write functionality here")
                        
                    elif(currentScreen == "table"):
                        print("Write functionality here")

                    elif(currentScreen == "training"):
                        #Will start training of the word Up
                        pass

                elif buttons[3].collidepoint(mouse_pos):
                    if(currentScreen == "main"):
                        print("Write functionality here")
                        
                    elif(currentScreen == "table"):
                        table.goDown(5)

                    elif(currentScreen == "training"):
                        #Will start training of the word Down
                        pass

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
                        pass 

                    
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

def stopButtonEventHandler():
    global currentScreen
    #Running through all events this iteration
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

                                                     
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

                if buttons[0].collidepoint(mouse_pos):
                    if(currentScreen == "stop"):
                        table.stopTable()
                        currentScreen = "main"
    return True

def stopButtonLayout(name, myfont, action):
    # create and display buttons
        buttons[0] = button(width/2*1-stopBtn_width/2, 80,
                           stopBtn_width, stopBtn_height, [255, 0, 0])

        # display text for buttons
        text(name, myfont, buttons[0].center)
        text(action, myfont, (width/2, 40))

def listeningLayout(action):
    font = pygame.font.SysFont("freesansbold", 45)
    text(action, font, (width/2, height/2))

def text(txt, font, location):
    text_to_display = font.render(txt, 1, (255, 255, 255))
    placement = (location[0]-text_to_display.get_rect().width/2,
                 location[1]-text_to_display.get_rect().height/2)
    screen.blit(text_to_display, placement)

def wait():
    global listening
    global tablelistening
    global currentScreen
    counter = 0
    while counter <= 100:
        time.sleep(0.1)
        counter += 1
    listening = False
    currentScreen = "main"


if __name__ == '__main__':
    main()
    
