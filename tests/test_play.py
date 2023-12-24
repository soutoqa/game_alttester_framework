import unittest
from alttester import *


class MyFirstTest(unittest.TestCase):
    altdriver = None

    @classmethod
    def setUpClass(cls):
        AltReversePortForwarding.reverse_port_forwarding_android()
        cls.altdriver = AltDriver()

    def test_start_game(self):
        self.altdriver.find_object(By.NAME, "StartButton").tap()

    def test_back_to_main_menu(self):
        self.altdriver.find_object(By.NAME, "pauseButton").tap()
        self.altdriver.find_object(By.NAME, "Exit").tap()
        self.altdriver.find_objects(By.NAME, 'CharName')
        self.assertEqual(AltObject.name, "TRASH CAT")
