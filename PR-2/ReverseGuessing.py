import random    # random number generator module
import math

# print the program heading
print ("Welcome to the Reverse Guessing Game!\n")

# computer picks a number between 1 and 1000
#selection
numberOfAttempts = int(input("How many Games would you like to play? "))

#highLow will be user input to state h,l,e
#variables
highLow=""

#event
for i in range(numberOfAttempts):
  tries=0
  #target value for computer to hit
  target = int(input("Choose a number between 1 and 1000 inclusive, and I (the computer) will try to guess it. "))
  min,max=1,1000
  guess = random.randint(min,max)
  print("My guess is {}".format(guess))
  #guessing loop or iteration
  while True:
    highLow=input("Is my guess to (h)high , too (l)low, or (e)equal to your number? ")
    #conditional
    if highLow=="h":
      max=guess 
    elif highLow=="l":
      min=guess
    elif highLow=="e":
      print("I win!  It took me {} guess(es)".format(tries))
      break
    guess = int((min+max)/2)
    print("My guess is {}".format(guess))
    tries+=1

'''
Difficulty in writing the assignment - Ususally I have to guess the number, so it
  is strange thinking of how to make the computer guess which number I had.

Easiest in writing the assignmnet - Luckily the flow followed the original
  version of the guessing game, so it was easy to start

Changes for next time - It would be nice to have the computer guess randomly or
  using the average.  If I were to assign this game, I would have my students
  add in this feature, and if we get to lists, have the computer store the values
  in memory and use that somehow to guess.

'''



