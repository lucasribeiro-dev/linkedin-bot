from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
import traceback
from singleton.singleton_meta import SingletonMeta
from util.logger import setup_logger
from config import config

class SeleniumWebdriver(metaclass=SingletonMeta):

    _driver = None
    _wait = None

    def __init__(self, headless=False):
        """
        Inicializa o WebDriver
        
        Args:
            headless (bool): Se deve executar em modo headless
        """
        self.logger = setup_logger()
        
        try:
            print("Starting WebDriver configuration...")
            
            chrome_options = Options()
            if headless:
                chrome_options.add_argument("--headless")

            user_data_dir = "__perfil__"

            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--remote-debugging-port=9222")
            chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
            chrome_options.add_argument("--profile-directory=Default")  
            
            chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

            print("Initializing WebDriver...")
            service = Service(executable_path=config['webdriver']['executable_path'])
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.wait = WebDriverWait(self.driver, 10)
            
            
            try:
                self.driver.get("https://www.linkedin.com")
                print("LinkedIn connection established!")
            except Exception as e:
                print(f"Error connecting to LinkedIn: {e}")
                raise
            
        except WebDriverException as e:
            print(f"WebDriver error: {e}")
            print("Full stack trace:")
            traceback.print_exc()
            raise
        except Exception as e:
            print(f"Error during WebDriver initialization: {e}")
            print("Full stack trace:")
            traceback.print_exc()
            print("Please check if:")
            print("1. Chromium is installed")
            print("2. ChromeDriver is installed and in PATH")
            print("3. Chromium and ChromeDriver versions are compatible")
            raise

    def driver(self): return self._driver

    def wait(self): return self._wait
