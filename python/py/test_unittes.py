import unittest

from bank_account import BankAccount

class AccountBalanceTestCase(unittest.TestCase):
    def setUp(self):
        self.account_yangu = BankAccount()

    def test_balance(self):
        self.assertEqual(self.account_yangu.balance, 3000, msg = 'Balance invalid')

    def test_deposit(self):
        self.account_yangu.deposit(4000)
        self.assertEqual(self.account_yangu.balance, 7000, msg = 'some error occured')
