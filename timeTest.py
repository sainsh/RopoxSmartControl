import time
for x in range(10):
    millis = int(round(time.time() * 1000))
    print (millis % 1000)
    time.sleep(0.3)
    