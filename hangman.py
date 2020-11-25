import os
import random

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

# =========================================


# get lives funcionality =======
# lives = menu()
# print(lives)

word = get_word_to_quess()
print(word)
print(len(word))

# def play(word, lives = 7):
#     pass


# play('Codecool', 6)
