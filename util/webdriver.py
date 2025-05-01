import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def type_like_human(element, text):
        """
        Types text like a human, with small time variations between keystrokes
        
        Args:
            element: Selenium WebElement to type into
            text: String text to type
            
        Returns:
            None
        """
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(0.05, 0.15))

def random_delay(min_seconds=1.5, max_seconds=3.5):
        """
        Adds a random delay between actions to simulate human behavior
        
        Args:
            min_seconds (float): Minimum delay in seconds
            max_seconds (float): Maximum delay in seconds
        Returns:
            None
        """
        delay = random.uniform(min_seconds, max_seconds)
        time.sleep(delay)

def is_element_clickable(element):
        """
        Checks if a web element is clickable by verifying it is both displayed and enabled
        
        Args:
            element: Selenium WebElement to check
        Returns:
            bool: True if element is clickable, False otherwise
        """
        try:
            return element.is_displayed() and element.is_enabled()
        except:
            return False
        
def scroll_to_element(driver,element):
    """
    Scrolls the page to bring an element into view and moves the mouse to it
    
    Args:
        driver: Selenium WebDriver instance
        element: WebElement to scroll to
    Returns:
        None
    """
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    random_delay(1, 2)

    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    random_delay(1, 2)

def scroll_page(driver, num_scrolls=1):
        """
        Scrolls the page to load more content
        
        Args:
            driver: Selenium WebDriver instance
            num_scrolls (int): Number of times to scroll the page
        Returns:
            None
        """
        for _ in range(num_scrolls):
            driver.execute_script("window.scrollBy(0, 800);")
            random_delay(0.5, 1.5)

def next_page(driver):
     """
     Clicks the 'Next' button to navigate to the next page of results
     
     Args:
         driver: Selenium WebDriver instance
     Returns:
         None
     """
     button = driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'Next') or contains(@aria-label, 'next')]")
     print("BUTTON", button[0])
     button[0].click()