import os
import random
import pictures_state
from time import sleep

def clear_console():
    os.system('cls')

def display_difficulty_options():
    print("HANGMAN")
    print("=======")
    print("6 - easy")
    print("5 - medium")
    print("4 - hard")
    print("3 - very hard")

def get_lives():
    # numbers range between 3-6
    ascii_number_3 = 51
    ascii_number_6 = 54

    while True:
        lives = input("Choose game level: ")
        lives = lives[0:1]
        
        if lives == '':
            print("level can not be empty")
            continue

        if ord(lives) < ascii_number_3 or ord(lives) > ascii_number_6:
            print("level has to be between 3 - 6")
            continue
        
        break
    return int(lives)

def choose_difficulty_level():
    clear_console()   
    display_difficulty_options()
    lives = get_lives()
    return lives; 

def read_file(path):
    with open(path) as f:
        lines = f.readlines()
    return lines

def separate_countries(countries):
    tempCountries = []

    for item in countries:
        tempCountries.append(item.split(' ')[0])

    return tempCountries    

def select_countries_level(countries, level):
    tempCountries = []

    for item in countries:
        if(level <= 3):
            if(len(item) <= 6):
                tempCountries.append(item)
        if(level == 4):
            if(len(item) == 7):
                tempCountries.append(item)
        if(level == 5):
            if(len(item) == 8):
                tempCountries.append(item)
        if(level >= 6):
            if(len(item) >= 9):
                tempCountries.append(item)

    return tempCountries

def get_word_to_quess(level):
    path = 'countries-and-capitals.txt'

    countries = read_file(path)
    
    countries = separate_countries(countries)

    countries = select_countries_level(countries, level)

    word = random.choice(countries)
    
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

def display_current_state(guess_state, lives, used_letters, game_level):
    print("Current Game State: ")
    print("-------------------")
    print("")
    print(f"Lives left: {lives}")
    print(f"Used letters: {used_letters if len(used_letters) > 0 else ''}")
    print("")

    print(pictures_state.get_current_picture(lives, game_level))
    
    print(' '.join(guess_state))
    print("")

def get_next_letter():
    #letters range between a - z
    ascii_letter_a = 97
    ascii_letter_z = 122

    quit_game = False

    while True:
        letter_pressed = input("Add letter: ").lower()

        if letter_pressed == '':
            print('letter can not be empty')
            continue
        
        if letter_pressed == 'quit':
            quit_game = True
            return ('', quit_game)

        letter_pressed = letter_pressed[0:1]
        letter_ascii = ord(letter_pressed)
        
        if letter_ascii < ascii_letter_a or letter_ascii > ascii_letter_z:
            print('letter has to be at range of a-z or A-Z')
            continue

        break

    return (letter_pressed, quit_game)

def check_if_used_letter(used_letters):
    temp_used_letters = used_letters
    letter, quit_game = get_next_letter()

    while letter in temp_used_letters:
        print(f"You have already used letter: {letter}")
        letter, quit_game = get_next_letter()
        
    temp_used_letters.add(letter)

    return (letter, temp_used_letters, quit_game)

def check_letter_in_word(word, guess_state, guesses_left, letter):
    index = 0
    hit = False
    for item in word:
        if item.lower() == letter:
            guess_state[index] = item
            hit = True
        index += 1
    
    if not hit:
        clear_console()
        print(f"There is no letter: {letter}")
        guesses_left -= 1
        sleep(1)

    return (guess_state, guesses_left)

def lose_game(word):
    clear_console()
    print(pictures_state.get_loose_picture())
    print("Correct answear is:")
    print(''.join(word))

def win_game():
    clear_console()
    print(pictures_state.get_win_picture())

def repeat_game():
    quit_game = True
    while True:
        print()
        repeat = input("Repeat game (Y/N): ")

        if repeat == '':
            print('letter can not be empty')
            continue
        
        repeat = repeat[0:1].lower()

        if repeat == 'y':
            quit_game = False
        
        break
    return not quit_game
# =========================================

def play(word, lives = 6):
    clear_console()
    game_level = lives

    guesses_left = lives
    used_letters = set()
    word = change_word_to_list(word)
    guess_state = initial_quess_state(word)


    while True:
        clear_console()
        display_current_state(guess_state, guesses_left, used_letters, game_level)
        
        # get letter and check if already has been taken
        letter, used_letters, quit_game = check_if_used_letter(used_letters)

        if quit_game:
            clear_console()
            print(pictures_state.get_terminated_picture())
            return True

        guess_state, guesses_left = check_letter_in_word(word, guess_state, guesses_left, letter)

        if guesses_left == 0:
            lose_game(word)
            return False

        if word == guess_state:
            win_game()
            return False

def run_game():
    while True:
        lives = choose_difficulty_level()
        word = get_word_to_quess(lives)
        # quit_game = play(word, lives)
        quit_game = play('Codecool Fun', lives)
        if quit_game:
            break

        if(not repeat_game()):
            break

# ==========================================

run_game()


# play('Codecool', 6)
