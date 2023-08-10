import unittest
from account import Baccount

class TestBankAccount(unittest.TestCase):

    def test_init(self):
        account = BankAccount("John")
        self.assertEqual(account.get_name(), "John")
        self.assertEqual(account.getbalance(), 0)

    def test_deposit(self):
        account = BankAccount("John")
        self.assertTrue(account.deposit(100))
        self.assertEqual(account.getbalance(), 100)
        self.assertFalse(account.deposit(-50))
        self.assertEqual(account.getbalance(), 100)

    def test_withdraw(self):
        account = BankAccount("John")
        account.deposit(100)
        self.assertTrue(account.withdraw(50))
        self.assertEqual(account.getbalance(), 50)
        self.assertFalse(account.withdraw(100))
        self.assertEqual(account.getbalance(), 50)
        self.assertFalse(account.withdraw(-10))
        self.assertEqual(account.getbalance(), 50)

if __name__ == '__main__':
    unittest.main()
