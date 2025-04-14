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
    ''' Test cases for the reverse_word function '''
    def test_reverse_word(self):
        ''' Test the reverse_word function '''
        self.assertEqual(reverse_word("hello"), "olleh")
        self.assertEqual(reverse_word("W"), "W")
        self.assertEqual(reverse_word(""), "")
        self.assertEqual(reverse_word("12345"), "54321")
        self.assertEqual(reverse_word("hello world"), "dlrow olleh")

class TestReverseAllWords(unittest.TestCase):
    ''' Test cases for the reverse_all_words function '''
    def test_reverse_all_words(self):
        ''' Test the reverse_all_words function '''
        self.assertEqual(reverse_all_words("hello world"), "olleh dlrow")
        self.assertEqual(reverse_all_words("W"), "W")
        self.assertEqual(reverse_all_words(""), "")
        self.assertEqual(reverse_all_words("12345"), "54321")


class TestMainFunction(unittest.TestCase):
    ''' Test cases for the main function '''
    def test_main_prints_correct_output(self):
        ''' Test the main function with a sample input '''
        sys.argv = ['production.py', 'this', 'is', 'a', 'test']
        sys.stdout = StringIO()

        main()

        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "siht si a tset")

    def test_main_no_args(self):
        ''' Test the main function with no arguments '''
        sys.argv = ['production.py']  # No phrase provided
        sys.stdout = StringIO()

        main()

        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Provide a phrase.")

if __name__ == '__main__':
    unittest.main()
