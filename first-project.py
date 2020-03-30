
from threading import Thread
import time
from queue import Queue

down = 11 
up = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(down, GPIO.OUT)
GPIO.setup(up, GPIO.OUT)


# Global variabel(boolean) der styrer tråden
stop = False

def goDown():
    # Giver den globaler variabel til goDown-tråden 
    global stop
    counter = 0
    #Simulerer at GPIO tænder
    print("Tænder GPIO")
    GPIO.output(down, GPIO.HIGH)

    # Checker om loopet skal stoppes
    while not stop and counter <= 50:
        print("Kører ned " + str(counter))
        #Opdaterer hver 0.1 sekund
        time.sleep(0.1)
        counter += 1
    # Simulerer at GPIO slukker når 5 sekunder er gået, eller stop boolean er True
    GPIO.output(down, GPIO.low)
# Denne metode fungerer på samme måde som goDown
def goUp():
    global stop
    counter = 0
    print("Tænder GPIO")
    GPIO.output(up, GPIO.HIGH)
    while not stop and counter <= 50:
        print("Kører op " + str(counter))
        time.sleep(0.1)
        counter += 1
    print("Sluker GPIO")
    GPIO.output(up, GPIO.LOW)


if __name__ == "__main__":   
    if 'down' in readable_results:
        # opretter en tråd og starter den
        t = Thread(target = goDown, args =())
        t.start()
    elif 'up' in readable_results: 
        t = Thread(target = goUp, args= ())
        t.start()
    elif 'stop' in readable_results:
        # Den globale variabel stop sættes til True så trådene stopper eksekveringen
        stop = True 
        # Sover i 0.1 sekunder så tråden når at registrere at den skal stoppes
        time.sleep(0.1)
        # stop sættes til False, ellers kan tråden ikke starte et nyt loop hvor bordet kører op eller ned
        stop = False 
    
       
    



    


    
        
