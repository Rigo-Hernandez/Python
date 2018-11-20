import random
guesses = 0
correct= random.randint(1,10)
print("I am thinking of a number between 1 and 10. ")
while True:
    guessleft = 5- guesses
    print ("You have {} guesses left. ".format(guessleft))
    if guesses == 5:
        print ("You ran out of guesses. ")
        break
    while True:
        try:
            guess = int(input("Whats the number? "))
            break
        except ValueError:
            print ("that is not a number. ")
    guesses=guesses +1
    if guess == correct:
        print ("Winner! Winner! Chicken Dinner!")
        break
    elif guess < correct:
        print ("Too low, try again. ")
    elif guess > correct:
        print("Too high, try again. ")
    else:
        print("Try again. ")