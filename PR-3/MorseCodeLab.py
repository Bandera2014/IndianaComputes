#Python MorseCode Lab Starter

def morseA():
    return ".-"
def morseE():
    return "."
def morseO():
    return "---"
def morseT():
    return "-"

def testLoop():
    print(morseA() + morseE())
    print(morseT()+morseT()+morseE() + morseT()+morseT()+morseE())
    print(morseT()+morseE()+morseE() + morseO()+morseT()+morseE()+morseE())

def translateToMC(message):
    msg=""
    for i in range(len(message)):
        if message[i].tolower()=="a":
            msg+=morseA()
        elif message[i].tolower()=="e":
            msg+=morseE()
        elif message[i].tolower()=="o":
            msg+=morseO()
        elif message[i].tolower()=="t":
            msg+=morseT()
    print("The message '{}' in morse code is '{}'".format(message,msg))

'''
while True:    
    user_input = input("Enter a message using only a,t,e, and o or -1 to exit: ")    
    if(user_input == "-1"):        
        break    
    print("The message '{}' in morse code is '{}'".format(user_input, "your morse code will go here!"))

print("Finished with morse code")
'''