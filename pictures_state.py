import time
import os

win_game =  """
    ||=====|
    |/    
    || CONGRATULATIONS!
    || You won the game   
    ||  
==================  
"""


loose_game = """
    ||=====|
    |/     O
    ||   -{ }-
    ||    / \\
    || GAME OVER
==================     
"""
picture6 = """
    ||=====|
    |/     O
    ||   -{ }-
    ||    / 
    ||    
==================
"""
picture5 = """
    ||=====|
    |/     O
    ||   -{ }-
    ||    
    ||    
==================
"""
picture4 = """
    ||=====|
    |/     O
    ||   -{ }
    ||    
    ||    
==================
"""
picture3 = """
    ||=====|
    |/     O
    ||    { }
    ||  
    ||    
==================
"""
picture2 = """
    ||=====|
    |/     O
    ||   
    ||   
    ||    
==================
"""
picture1 = """
    ||=====|
    |/    
    ||   
    ||    
    ||  
==================  
"""

level_6 = [picture1, picture2, picture3, picture4, picture5, picture6]

def console_clear():
    os.system('cls')

def get_win_picture():
    return win_game

def draw_single_hangman(index):
    console_clear()
    print(hangman_list[index])


# def draw_hangman(hangman_list):
#     for item in hangman_list:
#         console_clear()
#         print(item)
#         time.sleep(2)

# draw_hangman(hangman_list)