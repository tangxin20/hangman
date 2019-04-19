def hangman(word):
    wrong = 0
    stages = ["",
              "                    ",
              " --------------------",
              " |         |         ",
              " |         |         ",
              " |         O         ",
              " |        /|\        ",
              " |        / \        ",
              " |                   ",
              "---------------------"
        ]
    rletters = list(word)
    board = [" _ "]*len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages)-1:
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            rletters[cind] = '$'
            board[cind] = char
        else:
            wrong += 1
            print("".join(board))
            e = wrong + 1
            print("\n".join(stages[0:e]))
        if " _ " not in board:
            print("You win!")
            print("".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[:wrong+1]))
        print("You lose! It was {}.".format(word))
import random
a = ["cat", "dog", "bird", "fish"]
b = random.sample(a, 1)
c = "".join(b)
hangman(c)