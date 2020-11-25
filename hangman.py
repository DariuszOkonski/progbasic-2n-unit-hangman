def get_lives():
    while True:
        lives = input("Choose game level: ")
        lives = lives[0:1]

        if(lives == ''):
            print("level can not be empty")
            continue

        if ord(lives) < 51 or ord(lives) > 55:
            print("level has to be between 3 - 7")
            continue
        return int(lives)

def menu():
    print("HANGMAN")
    print("=======")
    print("7 - very easy")
    print("6 - easy")
    print("5 - medium")
    print("4 - hard")
    print("3 - very hard")
    lives = get_lives()

    print(lives)
    print(type(lives))

def get_word_to_quess():

    return "Some world"

# =========================================


menu()





# def play(word, lives = 7):
#     pass


# play('Codecool', 6)
