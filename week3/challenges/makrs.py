def read_marks(player):
    playerMarks = []
    while True:
        menu = input(f"Input a mark for {player} > ")

        if menu == "" and player != []:
            print("Marks added.")
            print()
            break
        else:
            try:
                playerMarks.append(int(menu))
            except:
                if menu == "x":
                    playerMarks.append(None)
                else:
                    print("Input a whole number or x.")
                    print()
    return playerMarks

def best_mark(marksList):
    #best_mark = max(marksList)
    best_mark = 0
    for mark in marksList:
        if mark != None:
            if mark > best_mark:
                best_mark = mark
    return best_mark

def winner(playerA, playerB, bestScoreA, bestScoreB):
    if bestScoreA > bestScoreB:
        print(f"{playerA} wins with a mark of {bestScoreA}!")
    elif bestScoreB > bestScoreA:
        print(f"{playerB} wins with a mark of {bestScoreB}!")
    else:
        print("No winner! Your best mark is equal.")

marksA = read_marks("A")
marksB = read_marks("B")

bestA = best_mark(marksA)
bestB = best_mark(marksB)

winner("A", "B", bestA, bestB)