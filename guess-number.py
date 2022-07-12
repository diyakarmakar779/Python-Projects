import random

# A function to check whether a number guessed by a user is correct or not
def guess(x,y):
    random_number = random.randint(x,y)
    guess_number = 0

    while(random_number!=guess_number):
        guess_number = int(input(f"Guess a number between {x} and {y}: "))
        if guess_number > random_number:
            print("Guess lower")
        elif guess_number < random_number:
            print("Guess higher")

    print("You guessed it right!")

# A function to check whether a number guessed by a computer is correct or not
def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback!='c':
        if low!=high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high(H), too low(L) or correct(C): ").lower()
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1

    
    print(f"Yay! The computer your number {guess}, correctly!")



computer_guess(1000)