import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from util.webdriver import random_delay, scroll_page, is_element_clickable
from util.logger import setup_logger
from manager.interfaces.feed_like_manager_interface import IFeedLikeManager
from manager.base_manager import BaseManager

class FeedLikeManager(BaseManager,IFeedLikeManager):
    def __init__(self, min_likes=2, max_likes=3):
        super().__init__()
        self.target_likes = random.randint(min_likes, max_likes)
        self.min_likes = min_likes
        self.max_likes = max_likes
        
    def like_feed_posts(self):
        self.logger.info(f"Starting post liking process (between {self.min_likes} and {self.max_likes})")
        
        try:
            self.driver.get("https://www.linkedin.com/feed/")
            random_delay(3, 5)
            
            likes_count = 0
            scroll_count = 0
            max_scroll = 15
            
            while likes_count < self.target_likes and scroll_count < max_scroll:
                like_buttons = self.driver.find_elements(
                    By.XPATH, 
                    "//button[contains(@aria-label, 'React Like') and not(contains(@aria-pressed, 'true')) and not(contains(@aria-label, 'comment')) ]"
                )
                
                if not like_buttons:
                    scroll_page(1)
                    scroll_count += 1
                    random_delay(1, 2)
                    continue
                
                self._like_posts(like_buttons, likes_count)

                if likes_count < self.target_likes:
                    scroll_page(1)
                    scroll_count += 1
                    random_delay(1, 2)
            
            self.logger.info(f"Post liking process completed. {likes_count} posts liked.")
            
        except Exception as e:
            self.logger.error(f"Error during post liking process: {e}")

    def _like_posts(self, like_buttons, likes_count):
        for button in like_buttons:
            if likes_count >= self.target_likes:
                break
            
            try:
                post_element = button.find_element(By.XPATH, "./ancestor::div[contains(@data-urn, 'activity')]")
                
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                random_delay(1, 2)
                
                if is_element_clickable(button):
                    button.click()
                    likes_count += 1
                    self.logger.info(f"Post liked ({likes_count}/{self.target_likes})")
                    random_delay(2, 4)
            
            except NoSuchElementException:
                continue
            except Exception as e:
                self.logger.warning(f"Error liking post: {e}")
                continue