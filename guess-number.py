import random

def guess(x,y):
    random_number = random.randint(x,y)
    guess_number = 0

    while(random_number!=guess_number):
        guess_number = int(input(f"Guess a number between {x} and {y}: 3"))
        if guess_number > random_number:
            print("Guess lower")
        elif guess_number < random_number:
            print("Guess higher")

    print("You guessed it right!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback!='c':
        guess = random.randint(low,high)
        feedback = input(f"Is {guess} too high(H), too low(L) or correct(C): ").lower()
        if guess == 'h':
            high = guess-1
        elif guess == 'l':
            lower = guess+1

    
    print(f"Yay! The computer your number {guess}, correctly!")



computer_guess(10)