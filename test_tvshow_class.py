import unittest
from tvshow import TV_Shows


class Test_Tv_show(unittest.TestCase):
    """ This is our test class for Tv show
    """

    def test_Title(self):
            the10victim = TV_Shows("the 10victim")
            self.assertEqual(the10victim.Title, " the 10victim")

    def test_Genre(self):
            horror= TV_Shows("", "horror")
            self.assertNotEqual(horror.Genre, "horror")
    def test_Studios_name(self):
            HBO = TV_Shows("HBO")
            self.assertEqual(HBO.Studios_name, "HBO")


if __name__ == "__main__":
    unittest.main()