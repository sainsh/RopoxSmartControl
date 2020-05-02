from threading import Thread
import time
import RPi.GPIO as GPIO

down = 11
up = 13
listening = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(down, GPIO.OUT)
GPIO.setup(up, GPIO.OUT)
GPIO.setup(listening, GPIO.OUT)


# Global variabel(boolean) der styrer traaden
stop = False
isListening = False

def goDown():
    # Giver den globaler variabel til goDown-traaden
    global stop
    global isListening
    counter = 0
    #Simulerer at GPIO taender
    print("Taender GPIO")
    GPIO.output(down, GPIO.HIGH)
    isListening = False

    # Checker om loopet skal stoppes
    while not stop and counter <= 50:
        print("Korer ned " + str(counter))
        #Opdaterer hver 0.1 sekund
        time.sleep(0.1)
        counter += 1
    # Simulerer at GPIO slukker naar 5 sekunder er gaaet eller stop boolean er $
    GPIO.output(down, GPIO.LOW)


# Denne metode fungerer paa samme maade som goDown

def goUp():
    global stop
    global isListening
    counter = 0
    print("Taender GPIO")
    GPIO.output(up, GPIO.HIGH)
    isListening = False

    while not stop and counter <= 50:
        print("Korer op " + str(counter))
        time.sleep(0.1)
        counter += 1
    print("Sluker GPIO")
    GPIO.output(up, GPIO.LOW)
    

def listen():
    global stop
    global isListening
    counter = 0
    print("Taender GPIO")
    GPIO.output(listening, GPIO.HIGH)
    while not stop and isListening and counter <= 100:
        print("Lytter " + str(counter))
        time.sleep(0.1)
        counter += 1
    print("Sluker GPIO")
    GPIO.output(listening, GPIO.LOW)
    isListening = False



def run(readable_results, data, rawbuf):
    global stop
    global isListening
    if 'ropox' in readable_results and isListening == False:
        isListening = True
        l = Thread(target = listen, args = ())
        l.start()
    if isListening:
        if 'down' in readable_results:
        # opretter en traad og starter den
                t = Thread(target = goDown, args =())
                t.start()
        elif 'up' in readable_results:
                t = Thread(target = goUp, args= ())
                t.start()
    if 'stop' in readable_results:
    # Den globale variabel stop saettes til True saa traadene stopper eksek$
            stop = True
            isListening = False
                # Sover i 100 milisekunder saa traaden naar at registrere at de$
            time.sleep(0.1)
    # stop saettes til False, ellers kan traaden ikke starte et nyt loop hv$
            stop = False



