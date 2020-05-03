import gui
from threading import Thread

if __name__ == '__main__':
    l = Thread(target = gui.main, args=())
    l.start()