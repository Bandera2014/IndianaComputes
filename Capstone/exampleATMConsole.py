"""
    1: first enter your username
    2: then ask for password
        if they enter it incorrectly 3 times shutdown the program
    3: print out their name and ask what they want to do/ create a transaction variable and make sure it doesn't go over 3
        deposit
            -ask how much they are depositing
            -add it to their balance
            -print their new balance in that account
            --have a back button
        withdrawal
            -create a enter your own option 
            -can't be over 500
            -show new balance in that account
            -have a back button
        balanceinquiry
            -print out the savings and checking balance
            -show new balance
            -have a back button
        transfer balance
            -can't be over 500
            -have a back button

        change pin
            -ask for new pin
            -print your new pin is...
            --have a back button
        log out
            -update the text file            -goes back to the username screen
"""
from MacdonaldCustomerClass import Customer 

#variables

filename="ATMCustomers.txt"
logOutMode=False         #this will keep the program running 



#functions

def deposit(moneyAccount):
    insert=input("How much money do you want to deposit? ")
    while (not insert.isdigit()):                               #this will make sure they input a number
        insert=input("How much money do you want to deposit? ")
    if moneyAccount=="s":
        customer.savings+=int(insert)                                   #this will add the money to that persons account
    elif moneyAccount=="c":
        customer.checkings+=int(insert)


def withdrawal(moneyAccount):
    takeOut=input("How much money do you want to withdrawel? ")
    while (not takeOut.isdigit()):                                      #this will make sure its a number
        takeOut=input("How much money do you want to withdrawel? ") 
    while int(takeOut)>=500:                                            #this will make sure they dont take out more than 500
        print("You can not take out that much")
        takeOut=input("How much money do you want to withdrawel? ")
    if moneyAccount=="s":
        customer.savings-=int(takeOut)  
        if customer.savings<10:                                                     #this makes sure that after they take the money out that they don't have less than 10 in their account
            print("You must have a minimum of $10 in your account. It did not withdrawel anything")
            customer.savings+=int(takeOut)                                          #if there is less than 10 in the account it will add the money back and say that you couldn't do that
    if moneyAccount=="c":
        customer.checkings-=int(takeOut)  
        if customer.checkings<10:                                                     #this makes sure that after they take the money out that they don't have less than 10 in their account
            print("You must have a minimum of $10 in your account. It did not withdrawel anything")
            customer.checkings+=int(takeOut)                                          #if there is less than 10 in the account it will add the money back and say that you couldn't do that
    

def balanceInquiry():
    print("Savings: ", customer.savings)
    print("Checkings: ", customer.checkings)

def transferBalance(moneyFrom):
    moneyAmount=input("How much money do you want to transfer? ")
    while (not moneyAmount.isdigit()):                                  #this will make sure its a number
        moneyAmount=input("How much money do you want to transfer? ")
    while int(moneyAmount)>=500:                                        #this will make sure its not more than 500
        print("You can not take out that much")
        moneyAmount=input("How much money do you want to transfer? ")
    if moneyFrom=="s":
        customer.savings-=int(moneyAmount)                                         #this will take the amount of money out of the account they want
        if customer.savings<10:                                                #this makes sure that after they take the money out that they don't have less than 10 in their account
            print("You must have a minimum of $10 in your account. It did not withdrawel anything")
            customer.savings+=int(moneyAmount)                                 #if there is less than 10 in the account it will add the money back and say that you couldn't do that
        else:
            customer.checkings+=int(moneyAmount)                               #it will add the amount to the account that they want
    elif moneyFrom=="c":
        customer.checkings-=int(moneyAmount)                                         #this will take the amount of money out of the account they want
        if customer.checkings<10:                                                #this makes sure that after they take the money out that they don't have less than 10 in their account
            print("You must have a minimum of $10 in your account. It did not withdrawel anything")
            customer.checkings+=int(moneyAmount)                                 #if there is less than 10 in the account it will add the money back and say that you couldn't do that
        else:
            customer.savings+=int(moneyAmount)                               #it will add the amount to the account that they want
          
    
    

def changePin():
    newPin=input("What do you want your new pin to be? ")
    while len(newPin)!=4:                                   #this will make sure the new pin is 4 digits long
        print("Your pin must be 4 numbers long")
        newPin=input("What do you want your new pin to be? ")
    while (not newPin.isdigit()):                           #this will make sure it is a number
        print("Your pin must be numbers")
        newPin=input("What do you want your new pin to be? ")
    customer.pin=newPin                                              #this will update the pin to the new one
    

           
    






creditCard=input("What is your cretit card: ")
file=open(filename,"r")         #this will open the file and read it
for line in file:
    temp=line.split(",")        #this will split the line from the commas
    if temp[0]!="Customer":         #this will skip the first line
        customer=Customer(temp[0].strip(),temp[1].strip(),temp[2].strip(),temp[3].strip(),temp[4].strip(),temp[5].strip(),temp[6].strip())          #this will strip the spaces from each variable
        if creditCard==((customer.creditCard)):             #this will make sure if the credit card is in the data base
            #print(customer.username)                #THIS NEEDS TO BE CREDIT CARD AND PIN TO LOG IN
            #print("got it")
            pinCount=3                 
            pinInput=input("What is your pin? ")          #if it is it will ask for the password
            while pinInput!=customer.pin:             #if the pin does not match then it will subtract 1 from the pinCount and keep asking until pinCount is at 0
                pinCount-=1
                print(f"That was not the right pin. You have {pinCount} tries left" )
                if pinCount==0:
                    print("You have been logged out")
                    logOutMode=False
                    break
                else:
                    pinInput=input("What is your pin: ")
            if pinInput==customer.pin:                #if the pin matches it will turn on logOutMode and reset the transactionNumber
                logOutMode=True
                transactionNumber=3
                #print("Correct")
                break
        """else:                                       #if it doesn't find the credit card in the data base it will tell them and break the loop
            print("You are not in the database")
            logOutMode=False
            break"""
                    
file.close()
while logOutMode==True:
    print(f"You have {transactionNumber} transactions left")            #this will print how many transactions they have left
    transaction=input("""What transaction would you like to do:             
    Deposit
    Withdrawal
    Balance Inquiry
    Transfer Balance
    Change Pin
    Log Out 

    """).lower()
    if transactionNumber==0:                            #if they are out of transactions it will stop the program
        print("You are out of transactions. You will be logged out")
        logOutMode=False
    elif transaction=="deposit":
        depositChoice=input("Which account? Savings(s) or Checkings(c) ").lower()       #this will ask what account they want and make sure its those 2. 
        if depositChoice=="s":
            deposit("s")
            transactionNumber-=1
        elif depositChoice=="c":
            deposit("c")
            transactionNumber-=1
        else:                                   #if its not s or c it will print that those weren't the options 
            print("That wasn't an option. It failed to deposit anything")
        print("Savings: ", customer.savings)
        print("Checkings: ", customer.checkings)
    elif transaction=="withdrawal":
        withdrawalChoice=input("Which account? Savings(s) or Checkings(c) ").lower()            #this will ask what account they want and make sure its those 2.
        if withdrawalChoice=="s":
            withdrawal("s")
            transactionNumber-=1
        elif withdrawalChoice=="c":
            withdrawal("c")
            transactionNumber-=1
        else:                                                           #if its not s or c it will print that those weren't the options
            print("That wasn't an option. It failed to withdrawal anything")
        print("Savings: ", customer.savings)
        print("Checkings: ", customer.checkings)
    elif transaction=="balance inquiry":
        balanceInquiry()
    elif transaction=="transfer balance":
        moneyFrom=input("What account do you want to take money from? Savings(s) or Checkings(c) ")         #this will ask what account they want and make sure its those 2.
        if moneyFrom=="s":
            transferBalance("s")
            transactionNumber-=1
        elif moneyFrom=="c":
            transferBalance("c")
            transactionNumber-=1
        else:                                                               #if its not s or c it will print that those weren't the options
            print("That wasn't an option. It failed to transfer anything")
        print("Savings: ", customer.savings)
        print("Checkings: ", customer.checkings)
    elif transaction=="change pin":
        changePin()
        print(f"Your new pin is {customer.pin}")
    elif transaction=="log out":
        print("loging out...")                 #this will change the logOutMode which will break the loop
        logOutMode=False
    
    
file=open(filename,"r+")
#file.write("Title,Author,Genre,isbn,Rating")
for line in file:
    temp=line.split(",")        #this will split the line from the commas
    if temp[0]==customer.customer:
        file.write(customer.fileFormat())
        break
file.close()    



    

