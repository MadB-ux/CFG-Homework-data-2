# Question 1
# Use the Simple ATM program to write unit tests for your functions.
# You are allowed to re-factor your function to ‘untangle’ some logic into smaller blocks of code to make it easier to write tests.
# Try to write at least 5 unit tests in total covering various cases. 

from unittest import TestCase, main
from ATM_task2 import pin_valid, withdraw

class TestWithdrawFunction(TestCase):

    def test_withdraw_less_than_balance(self):
        expected = 40.0
        result = withdraw(with_amount='60', acc_balance=100)
        self.assertEqual(expected, result)

    def test_withdraw_more_than_balance(self):
        expected = 100.0
        result = withdraw(with_amount='120', acc_balance=100)
        self.assertEqual(expected, result)
    
    def test_withdraw_negative_amount(self):
        expected = 100.0
        result = withdraw(with_amount='-100', acc_balance=100)
        self.assertEqual(expected, result)

    def test_withdraw_not_numerical_value(self):
        expected = 100.0
        result = withdraw(with_amount='hello', acc_balance=100)
        self.assertEqual(expected, result)

class TestPinValidFunction(TestCase):
    def test_pin_valid(self):
        expected = True
        result = pin_valid(pin_input='0000', pin_correct='0000')
        self.assertEqual(expected, result)
    
    def test_pin_invalid(self):
        expected = False
        result = pin_valid(pin_input='1111', pin_correct='0000')
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()