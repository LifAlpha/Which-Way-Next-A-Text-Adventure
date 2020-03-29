import os, time

#title screen holds for 5 seconds
print("Which Way Next: A Text Adventure Game\n")
print("A Python Project by Caroline Bowman\n")
print("Version 0.1\n")
time.sleep(5)

#clear the screen
os.system('cls')

#game start
from player import wwn_player
import wwn_world

