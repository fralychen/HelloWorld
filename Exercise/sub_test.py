from Exercise.sub import SubMain
import unittest
from unittest.main import main

class Testsub(unittest.TestCase):
    def test_init(self):
        s = SubMain()
    
    def test_num(self):
        s = SubMain()
        s.num()