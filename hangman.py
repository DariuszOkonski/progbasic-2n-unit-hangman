import os
import random

def clear_console():
    os.system('cls')

def display_menu_options():
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
        
        if(lives == ''):
            print("level can not be empty")
            continue

        if ord(lives) < ascii_number_3 or ord(lives) > ascii_number_7:
            print("level has to be between 3 - 7")
            continue
        
        break
    return int(lives)

def menu():
    os.system('cls')    
    display_menu_options()
    lives = get_lives()
    return lives; 

def read_file(path):
    with open(path) as f:
        lines = f.readlines()
    return lines

def get_word_to_quess():
    path = 'countries-and-capitals.txt'

    countries = read_file(path)
    single_country = random.choice(countries)
    
    word = single_country.split(' ')[0]

    return word

def change_word_to_list(word):
    return list(word)

def initial_quess_state(word):
    quess_state = []
    for item in word:
        if item == ' ':
            quess_state.append(' ')
        else:
            quess_state.append('_')
    return quess_state

def display_current_state(word, lives):
    print("Current Game State: ")
    print("-------------------")
    print("")
    print(f"Lives left: {lives}")
    print(' '.join(word))
    print("")

# =========================================

def play(word, lives = 7):
    clear_console()

    word = change_word_to_list(word)
    guess_state = initial_quess_state(word)

    display_current_state(guess_state, lives)

    # print(word)
    # print(guess_state)

    # print(type(word), word, len(word))
    # print(type(lives), lives)
    pass


def run_game():
    # lives = menu()
    # word = get_word_to_quess()
    # play(word, lives)
    play('Hong Kong', 5)
    # play('Polska', 5)

# ==========================================

run_game()


# play('Codecool', 6)
