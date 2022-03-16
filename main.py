import random

secret_number = random.randint(1,10)
guess_limit = 3
guess_count = 0
while guess_limit > guess_count:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You Win!")
        break
else:
    print("You lose....")
