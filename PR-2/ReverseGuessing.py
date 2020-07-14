import random    # random number generator module
import math

# print the program heading
print ("Welcome to the Reverse Guessing Game!\n")

# computer picks a number between 1 and 1000
numberOfAttempts = int(input("How many Games would you like to play? "))

#highLow will be user input to state h,l,e
highLow=""

for i in range(numberOfAttempts):
  tries=0
  #target value for computer to hit
  target = int(input("Choose a number between 1 and 1000 inclusive, and I (the computer) will try to guess it. "))
  min,max=1,1000
  guess = random.randint(min,max)
  print("My guess is {}".format(guess))
  #guessing loop
  while True:
    highLow=input("Is my guess to (h)high , too (l)low, or (e)equal to your number? ")
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
    