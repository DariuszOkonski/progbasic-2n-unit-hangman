import os

def display_menu():
    print("HANGMAN")
    print("=======")
    print("7 - very easy")
    print("6 - easy")
    print("5 - medium")
    print("4 - hard")
    print("3 - very hard")

def get_lives():
    ascii_number_3 = 51
    ascii_number_7 = 55

    while True:
        lives = input("Choose game level: ")
        lives = lives[0:1]
        
        # os.system('cls')
        
        if(lives == ''):
            # display_menu()
            print("level can not be empty")
            continue

        if ord(lives) < ascii_number_3 or ord(lives) > ascii_number_7:
            # display_menu()
            print("level has to be between 3 - 7")
            continue
        
        break
    return int(lives)

def menu():
    os.system('cls')    
    display_menu()
    lives = get_lives()
    return lives; 


def get_word_to_quess():

    return "Some world"

# =========================================


lives = menu()
print(lives)





# def play(word, lives = 7):
#     pass


# play('Codecool', 6)
