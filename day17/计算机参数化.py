import unittest
from ddt import ddt
from ddt import data
from ddt import unpack
from 计算器 import Calculator
import xlrd
da = []
wb = xlrd.open_workbook(filename="计算器数据.xls",encoding_override="True")
sheet = wb.sheet_by_index(0)
rows = sheet.nrows
for i in range(rows):
    da.append(sheet.row_values(i))

@ddt
class Calu(unittest.TestCase):
    @data(*da)
    @unpack
    def test_Ca(self,a,b,c):
        c1 = Calculator()
        s = c1.Add(a,b)
        self.assertEqual(c,s)











