print('Bot: I am thinking a number')
import random

number = random.randint(1,20)
guess =0

while guess != number:
    
  guess = int(input("ENTER GUESS: "))

  if (guess < number):
     print("Guess a higher number!")
  elif (guess > number):
    print("Guess a lower number!")
  else:    
     print ("Congratulation! you have guess a number")  