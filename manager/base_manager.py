from manager.interfaces.base_manager_interface import IBaseManager
from util.logger import setup_logger
from webdriver.selenium_webdriver import SeleniumWebdriver
from config import config

class BaseManager(IBaseManager):
    def __init__(self, driver=None, wait=None, logger=None):
        if driver and wait and logger:
            self._driver = driver
            self._wait = wait
            self._logger = logger
        else:
            webdriver = SeleniumWebdriver(config['settings']['headless_mode'])
            self._driver = webdriver.driver
            self._wait = webdriver.wait
            self._logger = setup_logger()

    @property
    def driver(self): return self._driver

    @property
    def wait(self): return self._wait

    @property
    def logger(self): return self._logger