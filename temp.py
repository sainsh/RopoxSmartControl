import os

# Method that takes a command line command and executes it
# @param command: the command to be executed
def runCommand(command): 
    #run command
    os.system(command)

# Will contain the command for training, without the acutaly training word. 
trainCommand = ""
# This will be changed to the correct path, when installing on a Raspberry
pathToSoparo = "/PATH/ "

# Will commence training of specified command in soparo: Such as "Ropox". Command example: commnandToTrain("Ropox")
def CommmandToTrain(word):
    runCommand("Echo " + pathToSoparo + trainCommand + word)

CommmandToTrain("Ropox")