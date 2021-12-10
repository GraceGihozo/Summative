import unittest
from music import Musics


class Test_Music(unittest.TestCase):
    """ This is our test class for Music
    """

    def test_init(test):
        def test_init(self):
            The100 = Musics("The 100")
            self.assertEqual(The100.Title, " The 100")
            horror = Musics("horror")
            self.assertNotEqual(horror.Genre, "horror")
            HBO = Musics("HBO")
            self.assertEqual(HBO.Studios_name, "HBO")


if __name__ == "__main__":
    unittest.main()