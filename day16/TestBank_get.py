import unittest
from bank import User_method
from bank import User

class TestBank_get(unittest.TestCase):
    def setUp(self) -> None:
        self.u = User_method()
        self.ur = User()

    def testGet(self):
        equ = 0
        self.ur.setId("12345670")
        self.ur.setPassword("111111")
        self.ur.setBalance("100")
        get = self.u.getmoney(self.ur)
        self.assertEqual(equ,get)
    def testGet1(self):
        equ = 1
        self.ur.setId("12345677")
        self.ur.setPassword("111111")
        self.ur.setBalance("100")
        get = self.u.getmoney(self.ur)
        self.assertEqual(equ, get)
    def testGet2(self):
        equ = 2
        self.ur.setId("12345670")
        self.ur.setPassword("111112")
        self.ur.setBalance("100")
        get = self.u.getmoney(self.ur)
        self.assertEqual(equ, get)
    def testGet4(self):
        equ = 3
        self.ur.setId("12345670")
        self.ur.setPassword("111111")
        self.ur.setBalance("1000")
        get = self.u.getmoney(self.ur)
        self.assertEqual(equ, get)






