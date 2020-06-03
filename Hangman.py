def hangman(word):
    wrong = 0
    stages = [
        "",
        "_________        ",
        "|                ",
        "|        |       ",
        "|        O       ",
        "|       /|\      ",
        "|       / \      ",
        "|                ",
    ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("    ")
    print("    ")
    print("    ")
    print("                                                                    Welcome to Hangman Game                            ")
    print("\n                                                                         ".join(stages[0: len(stages)]))
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter:"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("Game Over.")
        print("\n".join(stages[0: wrong+1]))
        print("You lose! It was {}.".format(word))

def play():
    n=input("Enter any 4 letter word:")
    hangman(n)

play()