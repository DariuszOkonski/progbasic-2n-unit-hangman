import os
import random
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
    # przyjmowanie liczb
    ascii_number_3 = 51
    ascii_number_6 = 54

    while True:
        lives = input("Choose game level: ")
        lives = lives[0:1]
        
        if lives == '':
            print("level can not be empty")
            continue

        if ord(lives) < ascii_number_3 or ord(lives) > ascii_number_6:
            print("level has to be between 3 - 7")
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

def display_current_state(guess_state, lives):
    print("Current Game State: ")
    print("-------------------")
    print("")
    print(f"Lives left: {lives}")
    print("")
    print(' '.join(guess_state))
    print("")

def get_next_letter():
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
        sleep(2)

    return (guess_state, guesses_left)

def lose_game(word):
    clear_console()
    print("YOU LOST GAME!!!")
    print("Correct answear is:")
    print(''.join(word))

def win_game():
    clear_console()
    print("CONGRATULATIONS!!! You won the game")

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

def play(word, lives = 7):
    clear_console()

    guesses_left = lives
    message = 'hello world'
    used_letters = set()
    word = change_word_to_list(word)
    guess_state = initial_quess_state(word)


    while True:
        clear_console()
        display_current_state(guess_state, guesses_left)
        
        # pobieramy literę i sprawdzamy czy była już pobrana
        letter, used_letters, quit_game = check_if_used_letter(used_letters)

        if quit_game:
            print(" === GAME TERMINATED BY USER === ")
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
        word = get_word_to_quess()
        quit_game = play(word, lives)
        # quit_game = play('Gliwice', lives)
        if quit_game:
            break

        if(not repeat_game()):
            break

# ==========================================

run_game()



# play('Codecool', 6)
