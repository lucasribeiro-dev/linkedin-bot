import traceback
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from util.webdriver import scroll_to_element, random_delay, scroll_page, is_element_clickable, next_page
from manager.interfaces.connect_with_people_interface import IConnectWithPeopleManager
from manager.base_manager import BaseManager

class ConnectWithPeopleManager(BaseManager,IConnectWithPeopleManager):
    def __init__(self,target_criteria=[]):
        super().__init__()

        self.target_criteria = target_criteria
        self.connections_made = 0 

    def connect_with_targets(self):
        self.logger.info(f"Starting connection with targets. Criteria: {self.target_criteria}")
        
        try:
            print("self._create_search_url()", self._create_search_url())
            self.driver.get(self._create_search_url())

            while self.connections_made != self.target_criteria['daily_connections']:
                random_delay(2, 4)
                
                scroll_page(self.driver, 3)
                
                connection_buttons = self.driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'connect') or contains(@aria-label, 'conectar')]")
                self.logger.info(f"Found {len(connection_buttons)} connection buttons")
                self._click_connections_button(connection_buttons)
                next_page(self.driver)
            
            self.logger.info(f"Connection process completed. {self.connections_made} connections made.")
            
        except Exception as e:
            self.logger.error(f"Error during connection process: {e}")

    def _create_search_url(self):
        base_url = "https://www.linkedin.com/search/results/people/?"
        
        param_mapping = {
            "keywords", "title", "company", "geoUrn", "activelyHiringForJobTitles"
        }
        
        query_params = [
            f"{key}={self.target_criteria[key]}" 
            for key in param_mapping 
            if key in self.target_criteria
        ]
        
        return base_url + "&".join(query_params)
        
    def _click_connections_button(self, connection_buttons):
        for button in connection_buttons:
            if self.connections_made >= self.target_criteria['daily_connections']:
                break
            
            try:
                scroll_to_element(self.driver, button)

                if is_element_clickable(button):
                    button.click()
                    random_delay(1, 2)
                    
                    try:
                        send_button = self.wait.until(EC.element_to_be_clickable(
                            (By.XPATH, "//button[contains(@aria-label, 'Enviar') or contains(@aria-label, 'Send without a note')]")
                        ))
                        send_button.click()
                        self.connections_made += 1
                        self.logger.info(f"Connection request sent ({self.connections_made}/{self.target_criteria['daily_connections']})")
                        random_delay(2, 4)
                    except TimeoutException:
                        self.logger.warning("Confirmation button not found")
                        continue
            
            except (ElementClickInterceptedException, NoSuchElementException) as e:
                self.logger.warning(f"Could not click connection button: {e}")
                continue
            except Exception as e:
                self.logger.error(f"Error trying to connect: {e}")
                continue