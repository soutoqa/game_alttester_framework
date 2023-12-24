import unittest
from pages.main_page import MainPage


class TestMainPage(unittest.TestCase):
    def test_success_play(self):
        main_page = MainPage()
        main_page.test_enter_to_settings()
        main_page.test_start_game()
