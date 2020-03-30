

#elements is a 2d array
def save_profile(profileName, elements): #element string format: bord x,skab y,ovn z ....
    lineNumber = check_profileName(profileName) 
    if  lineNumber > -1 :
       file = open("profiles.txt", "r") 
       fileLines = file.readlines()
       fileLines[lineNumber] = "{}, {}\n".format(profileName, elements) #replace the profile line with a new line with new input
       with open("profiles.txt", "w") as file : 
           file.writelines(fileLines)

    else:   #if no profile exists create a new
        file = open("profiles.txt", "a")
        file.write("{}, {}\n".format(profileName, elements))

#check if profile exists
def check_profileName(profileName) :
    file = open("profiles.txt", "r") 
    fileLines = file.readlines()
    i = 0
    for line in fileLines : #read every line
        words = line.split(",")
        if words[0] == profileName: #match profileName
            return i   #return line number
        i += 1

    return -1   #return -1 as no match


    
def read_profile(profileName):
    file = open("profiles.txt", "r")
    fileLines = file.readlines()
    commands = [] # array of commands

    for line in fileLines : 
        words = line.split(",")
        if words[0] == profileName: #check for profileName
            i = 0
            for command in words :
                if i != 0 :
                    commands.append("ropox {}".format(command)) # add each commands to array
                i += 1
    return commands
        


if __name__ == "__main__":  
    save_profile("hans", "bord 10,skab 205,ovn 402")
    save_profile("morten", "bord 123,skab 4523,ovn 456")
    save_profile("hans", "bord 100,skab 2005,ovn 4002")
    print (read_profile("hans"))
