import time
import os

terminated_game =  """
    ||=====|
    |/    
GAME TERMINATED BY USER
    || 
    ||  
==================  
"""

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

level_6 = [picture6, picture5, picture4, picture3, picture2, picture1]
level_5 = [picture6, picture5, picture4, picture2, picture1]
level_4 = [picture6, picture5, picture2, picture1]
level_3 = [picture6, picture2, picture1]

def get_win_picture():
    return win_game

def get_loose_picture():
    return loose_game

def get_terminated_picture():
    return terminated_game

def get_current_picture(index, level):
    if level == 6:
        return level_6[index - 1]
    if level == 5:
        return level_5[index - 1]
        return
    if level == 4:
        return level_4[index - 1]
    if level == 3:
        return level_3[index - 1]
    
    return "No such level"