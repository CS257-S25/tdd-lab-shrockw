'''
A file for tests for the production code.
'''
import unittest
import sys
from io import StringIO
from production import reverse_word
from production import reverse_all_words
from production import main

class TestReverseWord(unittest.TestCase):
    def test_reverse_word(self):
        self.assertEqual(reverse_word("hello"), "olleh")
        self.assertEqual(reverse_word("W"), "W")
        self.assertEqual(reverse_word(""), "")
        self.assertEqual(reverse_word("12345"), "54321")
        self.assertEqual(reverse_word("hello world"), "dlrow olleh")

class TestReverseAllWords(unittest.TestCase):
    def test_reverse_all_words(self):
        self.assertEqual(reverse_all_words("hello world"), "olleh dlrow")
        self.assertEqual(reverse_all_words("W"), "W")
        self.assertEqual(reverse_all_words(""), "")
        self.assertEqual(reverse_all_words("12345"), "54321")


class TestMainFunction(unittest.TestCase):
    def test_main_prints_correct_output(self):
        sys.argv = ['production.py', 'this', 'is', 'a', 'test']
        sys.stdout = StringIO()

        main()

        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "siht si a tset")

    def test_main_no_args(self):
        sys.argv = ['production.py']  # No phrase provided
        sys.stdout = StringIO()

        main()

        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Provide a phrase.")

    
if __name__ == '__main__':
    unittest.main()
