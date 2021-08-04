import unittest
from main import main
from unittest import mock
from unittest import TestCase


class TestMain(unittest.TestCase):

    def set_up(self):
        pass

    def test_user_quit(self):
        with mock.patch('builtins.input', return_value="quit"):
            self.assertEqual(main(), None)

    def test_menu_quit(self):
        with mock.patch('builtins.input', side_effect=["menu", "quit"]):
            self.assertEqual(main(), None)

    def test_input_1(self):
        with mock.patch('builtins.input', side_effect=["menu", "1", "1", "quit"]):
            self.assertEqual(main(), None)

    def test_input_1_failed_invalid(self):
        with mock.patch('builtins.input', side_effect=["menu", "1", "affas", "1", "quit"]):
            self.assertEqual(main(), None)

    def test_input_1_failed_outofbounds(self):
        with mock.patch('builtins.input', side_effect=["menu", "1", "7", "1", "quit"]):
            self.assertEqual(main(), None)

    def test_input_2(self):
        with mock.patch('builtins.input', side_effect=["menu", "2", "quit"]):
            self.assertEqual(main(), None)



if __name__ == '__main__':
    unittest.main()