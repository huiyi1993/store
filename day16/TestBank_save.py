import unittest
from bank import User_method
from bank import User

class TestBank_save(unittest.TestCase):
    def setUp(self) -> None:
        self.u = User_method()
        self.ur = User()

    def test_savve(self):
        equ = 1
        self.ur.setId("12345670")
        self.ur.setBalance(100)
        save = self.u.savemoney(self.ur)
        self.assertEqual(equ,save)

    def test_savve1(self):
        equ = 2
        self.ur.setId("12345673")
        self.ur.setBalance(100)
        save = self.u.savemoney(self.ur)
        self.assertEqual(equ, save)







