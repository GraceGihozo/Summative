import sys

from manager import Manager

class Customer(Manager):

    def requestitm(self,movie, TV_Shows, Musics, Video_game_disc):
        print("REQUESTING AN ITEM PROCESS \n_____________________________")
        type_item = input("PLEASE ENTER THE ITEM YOU ARE GOING TO BORROW: ")
        Name= input("Please enter your full name :")
        Email = input("Please enter your email personal")
        print(Name, "Welcome to Video store")
        print("This email", Email, "has been successfully ")
        # Request movies
        if type_item.lower() == "movie":

            print(Email)
            self.Title = input("Please enter the title of the movie: ")
            self.Genre = input("Please enter the genre of the movie: ")
            self.Duration = int(input("please enter minute of movie: "))
            self.published_year = input("When was the movie published: ")
            self.Studios_name = input("Please enter a name of studio movie produced in: ")
            self.Number_item = int(input("Please enter the number of movie you want: "))
            print("Thank you to borrow this movie :", self.Title, "Note:You suppose to return after 30 days")
            print("\n", len(movie))
        elif type_item.lower() == "tvshow":
            print("Please enter your full name ")
            print("Please enter your email personal")
            self.Title = input("Please enter the title of the tv show: ")
            self.Genre = input("Please enter the genre of the tv show: ")
            self.Duration = int(input("please enter minute of tv show: "))
            self.published_year = input("When was the tv show published: ")
            self.Studios_name = input("Please enter a name of studio tv show produced in: ")
            self.Number_item = int(input("Please enter the number of tv show you want: "))
            TV_Shows.remove(self)
            print("Thank you to borrow this tv show :", self.Title, "Note:You suppose to return after 30 days")
            print("\n", len(TV_Shows))
        elif type_item.lower() == "music":
            print("Please enter your full name like this GraceNimco")
            print("Please enter your email personal")
            self.Title = input("Please enter the title of the music: ")
            self.Genre = input("Please enter the genre of the music: ")
            self.Duration = int(input("please enter minute of music: "))
            self.published_year = input("When was the music published: ")
            self.Studios_name = input("Please enter a name of studio music produced in: ")
            self.Number_item = int(input("Please enter the number of music you want: "))
            Musics.remove(self)
            print("Thank you to borrow this tv show :", self.Title, "Note:You suppose to return after 30 days")
            print("\n", len(Musics))
        elif type_item.lower() == "videogame":
            print("Please enter your full name like this GraceNimco")
            print("Please enter your email personal")
            self.Title = input("Please enter the title of the music: ")
            self.Genre = input("Please enter the genre of the music: ")
            self.Duration = int(input("please enter minute of music: "))
            self.published_year = input("When was the music published: ")
            self.Studios_name = input("Please enter a name of studio music produced in: ")
            self.Number_item = int(input("Please enter the number of music you want: "))
            Video_game_disc.remove(self)
            print("Thank you to borrow this tv show :", self.Title, "Note:You suppose to return after 30 days")
            print("\n", len(Video_game_disc))
    def buyingitem(self,movie, TV_Shows, Musics, Video_game_disc):
        """ This method allow the customer to buy Item
        """
        print("BUYING AN ITEM PROCESS \n_____________________________")
        print("Please enter your full name like this GraceNimco")
        print("Please enter your email personal")
        print("please enter your credit card number")
        typeitem = input("PLEASE ENTER THE ITEM YOU ARE GOING TO BUY: ")
        if typeitem.lower() == "movie":
            selling_price = 2000
            print("This is price of each movie :", selling_price)
            titlemovie = input("PLEASE ENTER THE NAME MOVIE YOU WANT TO BUY: ")
            Number_itemmovie = int(input("Please enter the number of movies you want"))
            if titlemovie:
                buymovies = Number_itemmovie * selling_price
                print("Thank you for buying you will pay this amount:", buymovies)
        elif typeitem.lower() == "tvshow":
             selling_price = 4000
             print("This is price of each tv show :", selling_price)
             titletvshow = input("PLEASE ENTER THE NAME TV SHOW YOU WANT TO BUY: ")
             Number_itemtvshow = int(input("Please enter the number of  tv show you want"))
             if titletvshow:
                buytvshow = Number_itemtvshow * selling_price
                print("Thank you for buying you will pay this amount:", buytvshow)
        elif typeitem.lower() == "music":
             selling_price = 1000
             print("This is price of each album :", selling_price)
             titleMusic = input("PLEASE ENTER THE NAME MUSIC YOU WANT TO BUY: ")
             Number_itemMusic = int(input("Please enter the number of  music you want"))
             if titleMusic:
                buymusic = Number_itemMusic * selling_price
                print("Thank you for buying you will pay this amount:", buymusic)
        elif typeitem.lower() == "video_game_disc":
             selling_price = 10000
             print("This is price of each disc :", selling_price)
             titleVideogame = input("PLEASE ENTER THE NAME VIDEO GAME YOU WANT TO BUY: ")
             Number_itemVideogame = int(input("Please enter the number of  disc you want"))
             if titleVideogame:
                buymusic = Number_itemVideogame * selling_price
                print("Thank you for buying you will pay this amount:", buymusic)

    def returnitem(self, movie, TV_Shows, Musics, Video_game_disc):

        """ This method allow the customer to returning Item
        """
        print("RETURNING AN ITEM PROCESS \n_____________________________")
        type_item = input("PLEASE ENTER THE ITEM YOU'D LIKE TO RETURN: ")
        # Adding movies
        if type_item.lower() == "movie":
            self.Title = input("Please enter the title of the movie: ")
            self.Genre = input("Please enter the genre of the movie: ")
            self.Duration = int(input("please enter minute of movie: "))
            self.published_year = input("When was the movie published: ")
            self.Studios_name = input("Please enter a name of studio movie produced in: ")
            self.Number_item = int(input("Please enter the number of movie you want: "))
            self.selling_price = input("What is the Selling price of the movie: ")
            movie.append(self)
            print("Thanks for returning your borrowed movie:", self.Title)
            print("\n", len(movies))
            # Adding TV Show
        elif type_item.lower() == "tvshow":
            self.Title = input("Please enter the title of the Tv show: ")
            self.Genre = input("Please enter the genre of the Tv show: ")
            self.Studios_name = input("Please enter a name of studio did tv show produced in: ")
            self.selling_price = input("How much is the tv show sold for: ")
            self.Number_item = int(input("Please enter the number of tv show you want: "))
            self.Duration = input("please enter minute of tv show: ")
            self.published_year = input("When was the tv show published: ")
            self.Language = input("Please enter language Of tv shows :")
            TV_Shows.append(self)
            print("Thanks for returning your borrowed tv show:", self.Title)
            print("\n", len(TV_Shows))
            # Adding Music
        elif type_item.lower() == "Musics":
            self.Title = input("Please enter the title of the Musics: ")
            self.Genre = input("Please enter the genre of the musics: ")
            self.Studios_name = input("Please enter name of studio did music produced in: ")
            self.selling_price = input("How much is the musics sold for: ")
            self.Number_item = int(input("Please enter the number of music you want: "))
            self.Duration = input("please enter minute of musics: ")
            self.published_year = input("When was the music published: ")
            self.Language = input("Please enter language Of tv shows:")
            Musics.append(self)
            print("Thanks for returning your borrowed music:", self.Title, "")
            print("\n", len(Musics))
        elif type_item.lower() == "Video_game_disc":
            self.Title = input("Please enter the title of the video game: ")
            self.Genre = input("Please enter the genre of the video game: ")
            self.Studios_name = input("Please enter name of studio did video game produced in : ")
            self.selling_price = input("How much is the video game sold for: ")
            self.Number_item = int(input("Please enter the number of video game you want: "))
            self.Duration = input("How minute video game have: ")
            self.published_year = input("When was the video game published: ")
            self.Language = input("Please enter language Of video game:")
            Video_game_disc.append(self)
            print("Thanks for returning your borrowed video game :", self.Title)
            print("\n", len(Video_game_disc))


def main():
    movies = Manager()
    TV_Shows = Manager()
    Musics = Manager()
    Video_game_disc = Manager(["the100", "drama", 90, 2010, 2000, 100, "HBO", 1000],
                              ["gameover", "science fiction film", 90, 2011, 2000, 100, "amazon", 1000],
                              ["theGrinch", "Animation", 80, 2018, 2000, 100, "sony", 1000],
                              ["thenotebook", "rom-com ", 90, 2022, 2000, 100, "netflix", 1000],
                              ["F9", "action", 60, 2021, 2000, 100, "HBO", 1000])
    Client = Customer()
    done = False
    while not done:
        print(""" ======VIDEO STORE MENU=======
                  1. Display all available item
                  2. Request a item
                  3. Return a item
                  4. Buy a item
                  4. Exit
                  """)
        choice = int(input("Enter Choice:"))
        if choice == 1:
            movies.view(movies, TV_Shows, Musics, Video_game_disc)
            TV_Shows.view(movies, TV_Shows, Musics, Video_game_disc)
            Musics.view(movies, TV_Shows, Musics, Video_game_disc)
            Video_game_disc.view(movies, TV_Shows, Musics, Video_game_disc)
        elif choice == 2:
            movies.rent(Client.requestitm(movies, TV_Shows, Musics, Video_game_disc))
            TV_Shows.rent(Client.requestitm(movies, TV_Shows, Musics, Video_game_disc))
            Musics.rent(Client.requestitm(movies, TV_Shows, Musics, Video_game_disc))
            Video_game_disc.rent(Client.requestitm(movies, TV_Shows, Musics, Video_game_disc))

        elif choice == 3:
            movies.add(Client.returnitem(movies, TV_Shows, Musics, Video_game_disc))
            TV_Shows.add(Client.returnitem(movies, TV_Shows, Musics, Video_game_disc))
            Musics.add(Client.returnitem(movies, TV_Shows, Musics, Video_game_disc))
            Video_game_disc.add(Client.returnitem(movies, TV_Shows, Musics, Video_game_disc))

        elif choice == 4:
            movies.sell(Client.buyingitem(movies, TV_Shows, Musics, Video_game_disc))
            TV_Shows.sell(Client.buyingitem(movies, TV_Shows, Musics, Video_game_disc))
            Musics.sell(Client.buyingitem(movies, TV_Shows, Musics, Video_game_disc))
            Video_game_disc.sell(Client.buyingitem(movies, TV_Shows, Musics, Video_game_disc))
        elif choice == 4:
            sys.exit()

main()