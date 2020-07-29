#Python MorseCode Lab Starter
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
patterns=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
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
    for i in message.lower():
        msg+=patterns[alphabet.index(i)]
    print("The message '{}' in morse code is '{}'".format(message,msg))

while True:    
    user_input = input("Enter a message using only a,t,e, and o or -1 to exit: ")    
    if(user_input == "-1"):   
        break
    translateToMC(user_input)

print("Finished with morse code")
