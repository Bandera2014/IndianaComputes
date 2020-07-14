import random    # random number generator module
import math

# print the program heading
print ("Welcome to the Reverse Guessing Game!\n")

# computer picks a number between 1 and 1000
numberOfAttempts = int(input("How many Games would you like to play? "))

highLow=""



for i in range(numberOfAttempts):
  tries=0
  target = int(input('''Choose a number between 1 and 100 inclusive, and I (the computer) will try to guess it. '''))
  min,max=1,100
  guess = random.randint(min,max)
  print("My guess is {}".format(guess))
  correct=False
  while correct!=True:
    highLow=input("Is my guess to (h)high , too (l)low, or (e)equal to your number? ")
    if highLow=="h":
      print('elif high')
      max=guess
      
    elif highLow=="l":
      print('elif low')
      min=guess
      
    elif highLow=="e":
      print("I win!  It took me {} guess(es)".format(tries))
      correct=True
    guess = int((min+max)/2)
    tries+=1
    