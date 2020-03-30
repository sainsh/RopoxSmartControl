
#
#   Script that handles command line commands
#   
#   Author: @Cosby1992, @madsmansour, @DanORLarsen    
#

import os

# Method that takes a command line command and executes it on a thread
# @param command: the command to be executed

def runCommand(command): 
    #run command
    os.system(command)
