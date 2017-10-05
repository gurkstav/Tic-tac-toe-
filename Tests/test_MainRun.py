import unittest

from MainRun import *

class test_MainRun(unittest.TestCase):
    """
    Tests for MainRun.py
    """

    def test_set_main_menu(self):
        self.assertTrue(_name_process("foobar"))

if __name__ == '__main__':
    unittest.main()

