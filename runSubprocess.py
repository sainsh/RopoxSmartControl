import subprocess, sys, time
import json
import io

with io.open('./settings.json') as settingsFile:
    settings = json.load(settingsFile)
lang = settings['lang']
with io.open('./Localization/{}.json'.format(lang), encoding='utf8' ) as jsonFile:
    strings = json.load(jsonFile)


def run():

    #setting up the popen subprocess, cwd goes to another location before running the training command
    process = subprocess.Popen(('./sopare.py -l '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd="../sopare")
    
    while True:
        
        nextline = process.stdout.readline()

        if process.poll() is not None:
            break
        #decoding from bytes to string
        currentline = nextline.decode()
        #printing everything, not important but good for debugging
        print(currentline)
        #This is where our if/elif statements will control the GPIO pins when a specific word is recognized
        if("ropox" in currentline):
            sys.stdout.write(strings["text"]["working"])
            sys.stdout.flush()

    process.wait()
    output = process.communicate()[0]
    exitCode = process.returncode

    if(exitCode == 0):
        return output
    else:
        raise Exception("Failure, something went wrong")
    print("done")