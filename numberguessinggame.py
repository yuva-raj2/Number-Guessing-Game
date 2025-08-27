import random
def guessnum():
  number=random.randint(1,10)
  guess=None
  while(guess!=number):
    guess=int(input("Guess a number between 1 to 100:"))
    if(guess<number):
      print("Too low! Try again.")
    elif(guess>number):
      print("Too high! Try again.")
    else:
      print("Congratulations! You guessed the correct number.")
guessnum()