from typing import Protocol
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
import logging

class IBaseManager(Protocol):
    @property
    def driver(self) -> WebDriver: ...
    @property
    def wait(self) -> WebDriverWait: ...
    @property
    def logger(self) -> logging.Logger: ...