import random    # random number generator module

# print the program heading
print ("Welcome to the Guessing Game!\n")

# computer picks a number between 1 and 1000
target = random.randint(1, 1000)
print ("I (the computer) have chosen a number between 1 and 1000")

# ask the user for a number; must convert the input string into an integer
numberOfAttempts = int( input("How many times do you want to guess? "))
guess = 0
for i in range(numberOfAttempts):
  guess = int (input ("What is your guess? "))
  if guess==target:
    print("Congrats, you guessed it corectly!")
  elif guess<target:
    print("Your guess was to low")
  else:
    print("Your guess was to high")
print("Sorry you didn't guess it correctly. The number was {}".format(target))