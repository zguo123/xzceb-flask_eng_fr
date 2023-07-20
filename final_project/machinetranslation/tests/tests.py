import unittest

from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    """
    This class contains unit tests for the english_to_french function
    """

    def test_hello_bonjour(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_bye_aurevoir(self):
        self.assertEqual(english_to_french("Bye"), "Au revoir")


class TestFrenchToEnglish(unittest.TestCase):
    """
    This class contains unit tests for the french_to_english function
    """

    def test_bonjour_hello(self):

        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test_aurevoir_bye(self):
        self.assertEqual(french_to_english("Au revoir"), "Goodbye")


# run these tests
if __name__ == "__main__":
    unittest.main(verbosity=2)
