import random #imports the random library
randomNum = random.randint(0,9) #picks a random number between 0 and 9
GuessNumber = input("Guess the Digit:") #Users enters number to guess
guessNum = int(GuessNumber) #reads the input as integer

if randomNum == guessNum:
    print("Congratulations! Your Answer is PERFECT!") #prints if the guessed number and random number is equal
elif randomNum < guessNum:
    print("Your Answer is High than required") #prints if the randomnumber is less than guessed number
else:
    print("Your Answer is Less than required") #prints if the randomnumber is grater than guessed number
