import time
from alttester import *
from utilities import time


class MainPage:
    AltReversePortForwarding.reverse_port_forwarding_android()
    altdriver = AltDriver()

    SETTINGS_BTN = (By.NAME, 'SettingButton')
    CLOSE_SETTINGS = (By.NAME, 'CloseButton')
    RUN_BTN = (By.NAME, 'StartButton')
    PAUSE_BTN = (By.NAME, 'pauseButton')
    MAIN_MENU_BTN = (By.NAME, 'Text')

    def test_enter_to_settings(self):
        self.altdriver.find_object(*self.SETTINGS_BTN).tap()
        time.sleep()
        self.altdriver.find_object(*self.CLOSE_SETTINGS).tap()

    def test_start_game(self):
        time.sleep()
        self.altdriver.find_object(*self.RUN_BTN).tap()

