import random

print(f"{'GAME RULES!':^30}")
print()
print(f"You have 12 attempts to try and guess\nthe 4-digit number which contains numbers from 1 to 6.")
print()


def play():
    randomNumber = [random.randint(1, 6) for digit in range(4)]
    attempts = 0
    guess = ""
    print(randomNumber)

    while attempts < 12 and guess != randomNumber:
        while True:
            try:
                guess = [int(digit) for digit in input("Guess a 4-digit number: ")]
                if len(guess) != 4:
                    print("You have to guess a 4-digit number.")
                else:
                    attempts += 1
                    break
            except ValueError:
                print("That's not a number!")
        rightPlace = 0
        rightGuess = 0
        for i in range(4):
            if guess[i] in randomNumber:
                if guess[i] == randomNumber[i]:
                    rightPlace += 1
                else:
                    rightGuess += 1
        if rightPlace == 4:
            print(f"You win! It took you {attempts} attempts")
            print()
        else:
            print(f"{rightPlace} digits are in correct position, {rightGuess} digits are correct")

playing = True
while playing:
    menu = input("Play (p), Exit (e)\n> ").strip().lower()
    if menu == "p":
        play()
    elif menu == "e":
        print("Now exiting.")
        playing = False
    else:
        print("Wrong input.")
