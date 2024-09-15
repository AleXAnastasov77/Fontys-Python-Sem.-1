import random

print(f"{'GAME RULES!':^30}")
print()
print(f"You have 12 attempts to try and guess\nthe 4-digit number which contains numbers from 1 to 6.")
print()


def play():
    randomNumber = [random.randint(1, 6) for digit in range(4)]
    attempts = 0
    print(randomNumber)
    # Validating the input
    while True:
        try:
            guess = [int(digit) for digit in input("Guess a 4-digit number: ")]
            if len(guess) != 4:
                print("You have to guess a 4-digit number.")
            else:
                break
        except ValueError:
            print("That's not a number!")

    print(guess)


play()
