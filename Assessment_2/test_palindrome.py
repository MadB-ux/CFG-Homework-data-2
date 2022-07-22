from unittest import TestCase, main
from palindrome import palindrome

class TestPalindrome(TestCase):

    def test_valid_same_case_letters(self):
        expected = True
        result = palindrome(word='AVA')
        self.assertEqual(expected, result)

    def test_valid_different_case_letters(self):
        expected = True
        result = palindrome(word='Ava')
        self.assertEqual(expected, result)
    
    def test_even_number_of_letters(self):
        expected = True
        result = palindrome(word='Avva')
        self.assertEqual(expected, result)

    def test_odd_number_of_letters(self):
        expected = True
        result = palindrome(word='aVA')
        self.assertEqual(expected, result)

    def test_single_letter_word(self):
        expected = True
        result = palindrome(word='A')
        self.assertEqual(expected, result)

    def test_invalid_palindrome(self):
        expected = False
        result = palindrome(word='Hello')
        self.assertEqual(expected, result)
    
    def test_non_str_input(self):
        expected = True
        result = palindrome(word=1221)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()