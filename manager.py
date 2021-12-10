# Calling movies class
from Movies import movies
# Calling Music class

from music import Musics
# calling TV_Show class
from tvshow import TV_Shows
# Calling Video_game_discs class
from videogame import Video_game_disc
import pandas as pd

# Class Creation
class Manager (movies, TV_Shows, Musics, Video_game_disc):

    """ This is a  Manager Class with its characteristics
    """


    # Add method
    def add(self, movies, TV_Shows, Musics, Video_game_disc):
        """ This method allow the manager to add Item
        """
        print("ADDING AN ITEM PROCESS \n_____________________________")
        type_item = input("PLEASE ENTER THE ITEM YOU ARE GOING TO ADD: ")
        # Adding movies
        if type_item.lower() == "movie":
            self.Title = input("Please enter the title of the movie: ")
            self.Genre = input("Please enter the genre of the movie: ")
            self.Duration = int(input("please enter minute of movie: "))
            self.published_year = input("When was the movie published: ")
            self.Studios_name = input("Please enter a name of studio movie produced in: ")
            self.Number_item = int(input("Please enter the number of movie you want: "))
            self.selling_price = input("What is the Selling price of the movie: ")
            movies.append(self)
            print("YOU HAVE SUCCESSFULLY ENTERED:" , self.Title)
            print("\n" , len(movies))
        # Adding TV Show
        elif type_item.lower() == "tvshow":
            self.Title = input("Please enter the title of the Tv show: ")
            self.Genre = input("Please enter the genre of the Tv show: ")
            self.Studios_name = input("Please enter a name of studio did tv show produced in: ")
            self.selling_price = input("How much is the tv show sold for: ")
            self.Number_item = int(input("Please enter the number of tv show you want: "))
            self.Duration = input("please enter minute of tv show: ")
            self.published_year = input("When was the tv show published: ")

            TV_Shows.append(self)
            print("YOU HAVE SUCCESSFULLY ENTERED:" , self.Title)
            print("\n" , len(TV_Shows))
        # Adding Music
        elif type_item.lower() == "Musics":
            self.Title = input("Please enter the title of the Musics: ")
            self.Genre = input("Please enter the genre of the musics: ")
            self.Studios_name = input("Please enter name of studio did music produced in: ")
            self.selling_price = input("How much is the musics sold for: ")
            self.Number_item = int(input("Please enter the number of music you want: "))
            self.Duration = input("please enter minute of musics: ")
            self.published_year = input("When was the music published: ")

            Musics.append(self)
            print("YOU HAVE SUCCESSFULLY ENTERED:" , self.Title,"")
            print("\n" , len(Musics))
        # Adding Video game
        elif type_item.lower() == "Video_game_disc":
            self.Title = input("Please enter the title of the video game: ")
            self.Genre = input("Please enter the genre of the video game: ")
            self.Studios_name = input("Please enter name of studio did video game produced in : ")
            self.selling_price = input("How much is the video game sold for: ")
            self.Number_item = int(input("Please enter the number of video game you want: "))
            self.Duration = input("How minute video game have: ")
            self.published_year = input("When was the video game published: ")

            Video_game_disc.append(self)
            print("YOU HAVE SUCCESSFULLY ENTERED:" , self.Title)
            print("\n" , len(Video_game_disc))

    # Sell method
    def sell(self, movies, TV_Shows, Musics, Video_game_disc):
        """ This method allow the manager to sell Item
        """
        print("SELLING AN ITEM PROCESS \n_____________________________")
        typeitem = input("PLEASE ENTER THE ITEM YOU ARE GOING TO SELL: ")
        if typeitem.lower() == "movie":
            titlemovie = input("PLEASE ENTER THE MOVIE YOU WANT TO SELL: ")
            for x in movies :
              if titlemovie == x.Title:
                print(x.Title, "PRICE IS ", x.selling_price)
                x.Number_item = x.Number_item - 1
                print("THEY ARE", x.Number_item, "COPIES OF ", x.Title)
        elif typeitem.lower() == "tv_shows":
            titleTV_Show = input("PLEASE ENTER THE TV SHOW YOU WANT TO SELL: ")
            for x in TV_Shows:
              if titleTV_Show == x.Title:
                 print(x.Title, "PRICE IS ", x.selling_price)
                 x.Number_item = x.Number_item - 1
                 print("THEY ARE", x.Number_item, "COPIES OF ", x.Title)

        elif typeitem.lower() == "musics":
            titleMusics = input("PLEASE ENTER THE MUSIC YOU WANT TO SELL: ")
            for x in Musics:
              if titleMusics == x.Title:
                print(x.Title, "PRICE IS ", x.selling_price)
                x.Number_item = x.Number_item - 1
                print("THEY ARE", x.Number_item, "COPIES OF ", x.Title)

        elif typeitem.lower() == "video_game_disc":
            titleVideo_game_disc = input("PLEASE ENTER THE Video game YOU WANT TO SELL: ")
            for x in Video_game_disc:
              if titleVideo_game_disc == x.Title:
                print(x.Title, "PRICE IS ", x.selling_price)
                x.Number_item = x.Number_item - 1
                print("THEY ARE", x.Number_item, "COPIES OF ", x.Title)


    # Renting method
    def rent(self, movies, TV_Shows, Musics, Video_game_disc):
        """ This method allow the manager to rent Item
        """
        print("RENTING AN ITEM PROCESS \n_____________________________")
        typeitem = input("PLEASE ENTER THE ITEM YOU ARE GOING TO RENT: ")
        if typeitem.lower() == "movie":
            titlemovie = input("PLEASE ENTER THE MOVIE YOU WANT TO RENT:")
            for x in movies:
              if titlemovie == x.Title:
                print(x.Title , "RENTING PRICE IS " , x.rental_price)
                x.Number_item = x.Number_item - 1
                print("THEY ARE" , x.Number_item , "COPIES OF " , x.Title)

        elif typeitem.lower() == "tv_shows":
            titleTV_Shows = input("PLEASE ENTER THE TV SHOW YOU WANT TO RENT: ")
            for x in TV_Shows:
               if titleTV_Shows == x.Title:
                print(x.Title , "RENTING PRICE IS " , x.rental_price)
                x.Number_item = x.Number_item - 1
                print("THEY ARE" , x.Number_item , "COPIES LEFT OF " , x.Title)
        elif typeitem.lower() == "musics":
            titleMusics = input("PLEASE ENTER THE MUSIC YOU WANT TO RENT: ")
            for x in Musics:
              if titleMusics== x.Title:

                print(x.Title , "RENTING PRICE IS " , x.rental_price)
                x.Number_item = x.Number_item - 1
                print("THEY ARE" , x.Number_item , "COPIES LEFT OF " , x.Title)
        elif typeitem.lower() == "Video_game_disc":
            titleVideo_game_disc = input("PLEASE ENTER THE Video_game_disc YOU WANT TO RENT: ")
            for x in Video_game_disc:
               if titleVideo_game_disc == x.Title:

                print(x.Title , "RENTING PRICE IS " , x.rental_price)
                x.Number_item = x.Number_item - 1
                print("THEY ARE" , x.Number_item , "COPIES LEFT OF " , x.Title)


    # View method
    def view(self, movies, TV_Shows, Musics, Video_game_disc):
        """ View method help the Video store to view Item
        """
        print("YOU CAN VIEW ALL ITEMS FROM HERE \n--------------------------------")
        toview = input("WHICH ITEMS DO YOU WANT TO VIEW: ")
        if toview.lower() == "movie":
            print("\n ALL AVAILABLE MOVIE IN THE VIDEO STORE:", movies, "\n")

            for element in movies:
             print(element)


        elif toview.lower() == "tV_shows":
            print("\n ALL AVAILABLE TV SHOWS IN THE VIDEO STORE...... :", TV_Shows, "\n")

            for element in TV_Shows:
                print(element)

        elif toview.lower == "musics":
            print("\n ALL AVAILABLE MUSICS IN THE VIDEO STORE:", Musics, "\n")

            for element in Musics:
                print(element)

        if toview.lower == "video_game_disc":
            print("\n ALL AVAILABLE VIDEO GAME DISCS IN THE VIDEO STORE :", Video_game_disc, "\n")

            for element in Video_game_disc:
                print(element)



# movies =[["the100", "drama", 90, 2010, 2000, 100, "HBO", 1000],
#                     ["gameover", "science fiction film", 90, 2011, 2000, 100, "amazon", 1000],
#                     ["theGrinch", "Animation", 80, 2018, 2000, 100, "sony", 1000],
#                     ["thenotebook", "rom-com ", 90, 2022, 2000, 100, "netflix", 1000],
#                     ["F9", "action", 60, 2021, 2000, 100, "HBO", 1000]]
#
# TV_Shows =[["the100", "drama", 90, 2010, 2000, 100, "HBO", 1000],
#                        ["gameover", "science fiction film", 90, 2011, 2000, 100, "amazon", 1000],
#                        ["theGrinch", "Animation", 80, 2018, 2000, 100, "sony", 1000],
#                        ["thenotebook", "rom-com ", 90, 2022, 2000, 100, "netflix", 1000],
#                       ["F9", "action", 60, 2021, 2000, 100, "HBO", 1000]]
# Musics =[["the100", "drama", 90, 2010, 2000, 100, "HBO", 1000],
#                      ["gameover", "science fiction film", 90, 2011, 2000, 100, "amazon", 1000],
#                      ["theGrinch", "Animation", 80, 2018, 2000, 100, "sony", 1000],
#                      ["thenotebook", "rom-com ", 90, 2022, 2000, 100, "netflix", 1000],
#                     ["F9", "action", 60, 2021, 2000, 100, "HBO", 1000]]

# Video_game_disc = [["the100", "drama", 90, 2010, 2000, 100, "HBO", 1000],
#                               ["game_over", "science fiction film", 90, 2011, 2000, 100, "amazon", 1000],
#                               ["the Grinch", "Animation", 80, 2018, 2000, 100, "sony", 1000],
#                               ["the note book", "rom-com ", 90, 2022, 2000, 100, "netflix", 1000],
#                               ["F9", "action", 60, 2021, 2000, 100, "HBO", 1000]]


