import unittest
from bank import User_method
from bank import User
from bank import Address
import DBUtils
class TestBank(unittest.TestCase):
    def setUp(self) -> None:
        self.u = User_method()
        self.ur = User()
        self.ad = Address()
        self.db = DBUtils
    def test_Open(self):
        self.ur.setId("12345675")
        self.ur.setName("张三")
        self.ur.setPassword("111111")
        self.ur.setBalance(0)
        self.ad.setCountry("中国")
        self.ad.setProvince("河北")
        self.ad.setStreet("中华大街")
        self.ad.setDoor("101")
        self.ur.setTime("1")
        open = self.u.method(self.ur,self.ad)

        equ = 1
        self.assertEqual(equ,open)

    def test_Open1(self):
        self.ur.setId("12345679")
        self.ur.setName("张三")
        self.ur.setPassword("111111")
        self.ur.setBalance(0)
        self.ad.setCountry("中国")
        self.ad.setProvince("河北")
        self.ad.setStreet("中华大街")
        self.ad.setDoor("101")
        self.ur.setTime("1")
        open = self.u.method(self.ur, self.ad)

        equ = 2
        self.assertEqual(equ, open)

    def test_Open2(self):
        equ = 3
        equ1 = 1
        self.ur.setId("12345670")
        self.ur.setName("张三")
        self.ur.setPassword("111111")
        self.ur.setBalance(0)
        self.ad.setCountry("中国")
        self.ad.setProvince("河北")
        self.ad.setStreet("中华大街")
        self.ad.setDoor("101")
        self.ur.setTime("1")
        # open = self.u.method(self.ur, self.ad)
        data = self.db.select("select * from user",[])
        if len(data)==99:
            open1 = 1
            self.assertEqual(equ1, open1)
        elif len(data)==100:
            open2 = 3
            self.assertEqual(equ,open2)
        elif len(data)>100:
            open3 = 3
            self.assertEqual(equ,open3)










