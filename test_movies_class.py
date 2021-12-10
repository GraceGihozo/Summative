import unittest
from Movies import movies


class Test_movies(unittest.TestCase):
    """ This is our test class for audiobook
    """

    def test_init(test):
        def test_init(self):
            The100 = movies("The 100")
            self.assertEqual(The100.title, " The 100")
            horror = movies("horror")
            self.assertNotEqual(horror.genre, "horror")
            HBO = movies("HBO")
            self.assertEqual(HBO.Studios_name,"HBO")


if __name__ == "__main__":
    unittest.main()