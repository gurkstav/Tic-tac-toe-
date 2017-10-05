import unittest

from Tournament import *

class test_Tournament(unittest.TestCase):
    """
    Tests for Tournament.py
    """

    def test_ask_action(self):
        self.assertTrue(_name_process("foobar"))

if __name__ == '__main__':
    unittest.main()

