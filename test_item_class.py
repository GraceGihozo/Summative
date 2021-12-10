import unittest
from item import Item

class TestItem(unittest.TestCase):
    def test_title(self):
       testtitle = Item("the 10victim")
       self.assertEqual(testtitle.title, "the 10victim")

    def test_genre(self):
        testgenre = Item("", "horror")
        self.assertEqual(testgenre.genre, "", "horror")

    def test_Number_item(self):
        testNumber_item = Item("", "", 1, "", 0)
        self.assertNotEqual(testNumber_item.Number_item, "", 1, "", 0)


if __name__ == '__main__':
  unittest.main()
