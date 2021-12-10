import unittest
from videogame import Video_game_disc


class Test_Video_game_discs(unittest.TestCase):
    """ This is our test class for Video game
    """

    def test_init(test):
        def test_init(self):
            The100 = Video_game_disc("The 100")
            self.assertEqual(The100.Title, " The 100")
            horror = Video_game_disc("horror")
            self.assertNotEqual(horror.Genre, "horror")
            HBO = Video_game_disc("HBO")
            self.assertEqual(HBO.Studios_name, "HBO")



if __name__ == "__main__":
    unittest.main()