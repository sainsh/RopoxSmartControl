import subprocess, sys

#Just call this function with a string representing the word as parameter
def train(word):

#Sugggestion: Might need to add, a command that will stop and start the regular Soparo along with compile the new Data for use.    #By DanORLarsen

    #All words will be trained 5 times
    for i in range(5):
        print("starting process")

        #setting up the popen subprocess, cwd goes to another location before running the training command
        process = subprocess.Popen(('./sopare.py -v -t ' + word), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd="../sopare")
        
        while True:
            #Sopare sends all info we needs through the stderr and not stdout, be aware of this!
            nextline = process.stdout.readline()
            if process.poll() is not None:
                break
            currentline = nextline.decode()
            #Checks where we are in the trainingprocess
            if(currentline.__contains__("start endless")):
                sys.stdout.write("Sig " + word)
                sys.stdout.flush()
            if(currentline.__contains__("stop endless")):
                sys.stdout.write("Vent")
                sys.stdout.flush()
                
            

        process.wait()
        output = process.communicate()[0]
        exitCode = process.returncode

    if(exitCode == 0):
        return output
    else:
        raise Exception("Failure, something went wrong")
    print("done")
