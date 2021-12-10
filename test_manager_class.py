import unittest
from manager import Manager


class Test_Manager(unittest.TestCase):
    """ This a manager Test
    """

    def add(self):
        """ This a testing code of the add method
        """
        testmovie =Manager("movie")
        self.assertEqual(testmovie.add, "movie")
        self.assertNotEqual(testmovie.add, "movie")

    def sell(self):
        """ Testing code of sell method
        """
        testmusic = Manager("musics")
        self.assertEqual(testmusic.sell, "Musics")

    def rent(self):
        """ Testing code of rent method
        """
        testTV_Show = Manager("tv show")
        self.assertEqual(testTV_Show.rent, "tv show")

    def view(self):
        """ Testing code of view method
        """
        testVideo_game = Manager("video game")
        self.assertNotEqual(testVideo_game.view, "video game")

    def lend(self):
        """ Testing code of lend method
        """
        testVideo_game = Manager("video game")
        self.assertEqual(testVideo_game.Lend, "video game")

if __name__ == "__main__":
    unittest.main()