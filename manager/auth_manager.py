import traceback
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from util.webdriver import type_like_human,random_delay
from manager.interfaces.auth_manager_interface import IAuthManager
from manager.base_manager import BaseManager

class AuthManager(BaseManager,IAuthManager):

    def __init__(self, credentials):
        super().__init__()
        self.credentials = credentials

    def login(self):
        """Realiza login no LinkedIn

        Args:
            email (string): Credencial email para login
            password (string): Credencial senha para login
        """

        try:
            self.logger.info("Starting LinkedIn login process")
            self.driver.get("https://www.linkedin.com/login")

            if self.driver.current_url == "https://www.linkedin.com/feed/":
                return True
            
            username_input = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
            password_input = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
            
            type_like_human(username_input, self.credentials['email'])
            type_like_human(password_input, self.credentials['password'])
            
            login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            login_button.click()
            
            try:
                self.wait.until(EC.presence_of_element_located((By.ID, "global-nav")))
                print("Login successful")
                return True
            except TimeoutException:
                self.logger.error("Login failed: global navigation element not found")
                return False
                
        except Exception as e:
            traceback.print_exc()
            self.logger.error(f"Error during login: {e}")
            return False
        

    def logout(self):
        """Realiza logout do LinkedIn"""
        try:
            profile_menu = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@aria-label, 'Eu') or contains(@aria-label, 'Me')]")
            ))
            profile_menu.click()
            random_delay(1, 2)
            
            logout_button = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@href, 'logout')]")
            ))
            logout_button.click()
            random_delay(2, 3)
            
            self.logger.info("Logout successful")
            
        except Exception as e:
            self.logger.error(f"Error during logout: {e}")