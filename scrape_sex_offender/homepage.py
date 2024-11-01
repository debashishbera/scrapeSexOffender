from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import Locators      

class HomePage:
    def __init__(self, driver , browser):
        self.driver = driver
        self.browser = browser

    def enter_first_name(self, first_name):
        self.browser.enter_text(Locators.first_name_input_box , first_name)


    def enter_last_name(self, last_name):
        self.browser.enter_text(Locators.last_name_input_box , last_name)
  

    def enter_name(self, first_name , last_name):
         self.enter_first_name(first_name)
         self.enter_last_name(last_name)
    
    def click_on_search(self):
        self.browser.click_on(Locators.search_button)

    def search_the_name(self , first_name:str , last_name:str):
         self.enter_name(first_name , last_name)
         self.click_on_search()

    def is_results_not_present(self):
        try:
            no_results = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Locators.no_results)))
            #No results found
            self.browser.click_on(Locators.ok_button)
            #ok_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.ok_button)))
            #ok_button.click()
            return True
        except:
            #Results are present
            return False
