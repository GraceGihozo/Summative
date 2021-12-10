import pandas as pd
from ItemClass import Item
"""This is importing the item file to the tv show file 
"""



# Creating a child class
class TV_Shows(Item):
    """ This a TV SHOW class with its attributes
        """


    def __init__(self, Title="", Genre="", duration=0, Published_year=0, Selling_price=2000, studios_name="", number_item=100, rental_price=1000):
        super().__init__(Title, Genre, duration, Published_year, Selling_price)
        self.Studios_name = studios_name
        self.Number_item = number_item
        self.rental_price = rental_price

data = [["the100", "drama", 90, 2010, 2000, 100, "HBO", 1000],
        ["game_over", "science fiction film", 90, 2011, 2000, 100, "amazon", 1000],
        ["the Grinch", "Animation", 80, 2018, 2000, 100, "sony", 1000],
        ["the note book", "rom-com ", 90, 2022, 2000, 100, "netflix", 1000],
        ["F9", "action", 60, 2021, 2000, 100, "HBO", 1000]]

TV_Shows= pd.DataFrame(data, columns=["Title", "Genre", "duration", "Published_year", "Selling_price", "studios_name", "number_item", "rental_price"])
print(TV_Shows)
