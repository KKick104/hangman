def hangman(word):
    wrong = 0
    stages = ["",
              "_________       ",
              "|               ",
              "|       |       ",
              "|       O       ",
              "|      /|\      ",
              "|      / \      ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("welcome to Hangman")
    
