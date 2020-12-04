

# Imports
import random
# end Imports

# generate a random number between 1-100

# global variables
ComputerNumber = random.randint(1,100)

# this is an integer
GuessMax = 10

Win = False
Play = True

while Play == True:
  print("\nWelcome to the Great Number Guessing Game! \nYou have " + str(GuessMax) + " guesses. Use them carefully!")
  while GuessMax > 0:
    PlayerGuess = input("\nPlease enter a number between 1 and 100: ")
    PlayerGuess = float(PlayerGuess)

    if (PlayerGuess < 0 or PlayerGuess > 100):
      print("Oh no! That number won't work. Pick a number 1 - 100")
      break
    else:
      if PlayerGuess > ComputerNumber:
        print("Too big!")
        GuessMax = GuessMax - 1
        # GuessMax-- is the same effect as line 30
        print("You have " + str(GuessMax) + " guesses left!")
      elif PlayerGuess < ComputerNumber:
        print("That's too small!")
        GuessMax = GuessMax - 1 
        print("You have " + str(GuessMax) + " guesses left!")
      else:
        print("\nWow! You guessed it! Nice work!")
        Win = True
        print("You had " + str(GuessMax) + " guesses left.")
        GuessMax = 0
      

  if Win == True:
    
    break
  else: 
    print("No more guesses left!")
    print("The number was " + str(ComputerNumber) + ". Better luck next time!")
    break

answer = input("Would you like to play again? Y/N: ")

if answer == "N" or answer == "n" or answer == "No" or answer == "no":
  print("Ok, goodbye!")
  Play = False
else:
  Win = False
  GuessMax = 10