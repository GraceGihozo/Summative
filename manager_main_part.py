""" This our main program of Video store Management System, and this is importing all files to here
"""
from ItemClass import Item

from Movies import movies

from tvshow import TV_Shows

from music import Musics
from videogame import Video_game_disc

from manager import Manager



loop = True

while loop:
    print("\n----VIDEO STORE MANAGEMENT SYSTEM----\n")
    print("THE FOLLOWING ARE ITEMS IN THE VIDEO STORE")
    print("1. MOVIES \n2. TV SHOW \n3. MUSIC \n4.VIDEO GAME DISCS")
    print("\nFOLLOWING ARE ACTIONS YOU CAN MAKE ON ITEMS IN THE VIDEO STORE: ")
    print("1. ADD \n2. SELL \n3. RENT  \n4. VIEW ITEM")
    action = int(input("\nPLEASE ENTER THE NUMBER OF THE OPERATION YOU WANT TO MAKE: "))
    print("---------------------------------------------------------\n")
    if action == 1:
        new = Manager()
        new.add(movies, TV_Shows, Musics, Video_game_disc)

    elif action == 2:
        Sell = Manager()
        Sell.sell(movies, TV_Shows, Musics, Video_game_disc)

    elif action == 3:
        rent = Manager()
        rent.rent(movies, TV_Shows, Musics, Video_game_disc)

    elif action == 4:
        viewitem = Manager()
        viewitem.view(movies, TV_Shows, Musics, Video_game_disc)
