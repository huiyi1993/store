import unittest
from bank import User_method
from bank import User

class TestBank_transfer(unittest.TestCase):
    def setUp(self) -> None:
        self.u = User_method()
        self.ur = User()

    def testTransfer(self):
        equ = 0
        self.ur.setId("12345670")
        user = "12345671"
        self.ur.setPassword("111111")
        self.ur.setBalance(100)
        transfer = self.u.transfer(self.ur,user)
        self.assertEqual(equ,transfer)
    def testTransfer1(self):
        equ = 1
        self.ur.setId("12345678")
        user = "12345671"
        self.ur.setPassword("111111")
        self.ur.setBalance(100)
        transfer = self.u.transfer(self.ur, user)
        self.assertEqual(equ, transfer)

    def testTransfer2(self):
        equ = 2
        self.ur.setId("12345670")
        user = "12345671"
        self.ur.setPassword("111112")
        self.ur.setBalance(100)
        transfer = self.u.transfer(self.ur, user)
        self.assertEqual(equ, transfer)

    def testTransfer3(self):
        equ = 3
        self.ur.setId("12345670")
        user = "12345671"
        self.ur.setPassword("111111")
        self.ur.setBalance(1000)
        transfer = self.u.transfer(self.ur, user)
        self.assertEqual(equ, transfer)









