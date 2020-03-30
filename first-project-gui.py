import logging
from threading import Thread
import time
from queue import Queue
import logging
import tkinter as tk  
from tkinter import ttk
 
# Global variabel(boolean) der styrer tråden
stop = False
 
def goDown():
    # Giver den globaler variabel til goDown-tråden
    global stop
    counter = 0
    #Simulerer at GPIO tænder
    print("Tænder GPIO")
 
    # Checker om loopet skal stoppes
    while not stop and counter <= 50:
        print("Kører ned " + str(counter))
        #Opdaterer hver 0.1 sekund
        time.sleep(0.1)
        counter += 1
    # Simulerer at GPIO slukker når 5 sekunder er gået, eller stop boolean er True
    print("Sluker GPIO")
 
# Denne metode fungerer på samme måde som goDown
def goUp():
    global stop
    counter = 0
    print("Tænder GPIO")
    while not stop and counter <= 50:
        print("Kører op " + str(counter))
        time.sleep(0.1)
        counter += 1
    print("Sluker GPIO")
 
 
if __name__ == "__main__":  
 
    # tk ttk er GUI elementer og skal ikke indgå koden til Raspberryen
    win = tk.Tk()# Application Name  
    win.title("Python GUI App")# Label  
    lbl = ttk.Label(win, text = "Enter the name:").grid(column = 0, row = 0)# Click event
    # Click er en metode der bliver triggered når kanppen på GUIen klikkes
    # Dette simulerer at der kommer en kommando ind fra Sopare, men kommandoen har ikke samme format som fra Sopare  
    def click(event=None):  
        global stop
        # cmd trækker commandoen ud af Guien
        cmd = command.get()
        nameEntered.delete(0, 'end')
        # 3 if/else sætninger der checker kommandoen
        if cmd == "ned":
            # opretter en tråd og starter den
            t = Thread(target = goDown, args =())
            t.start()
        elif cmd == "op":
            t = Thread(target = goUp, args= ())
            t.start()
        elif cmd == "stop":
            # Den globale variabel stop sættes til True så trådene stopper eksekveringen
            stop = True
            # Sover i 0.1 sekunder så tråden når at registrere at den skal stoppes
            time.sleep(0.1)
            # stop sættes til False, ellers kan tråden ikke starte et nyt loop hvor bordet kører op eller ned
            stop = False
    # Resten af koden er GUI
    command = tk.StringVar()  
    nameEntered = ttk.Entry(win, width = 36, textvariable = command)# Button widget
    nameEntered.grid(column = 0, row = 1)  
    button = ttk.Button(win, text = "submit", command = click).grid(column = 1, row = 1)
    win.bind('<Return>', click)
    win.mainloop()