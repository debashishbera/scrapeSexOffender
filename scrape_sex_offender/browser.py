from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class BrowserActivities:
    def __init__(self, driver):
        self.driver = driver
        

    def click_on(self, xpath: str, count: int = 0) -> bool:
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
            return True
        except Exception as e:
            print(f"Attempt {count}: Unable to click on {xpath}")
            time.sleep(2)
            if count < 3:
                return self.click_on(xpath, count + 1)
            print(f"Final attempt failed to click on {xpath}")
            return False

    def enter_text(self, xpath:str , value:str):
        #import pdb; pdb.set_trace()
        try:
           element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
           element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
           element.send_keys(value)
        except:
             print(f"Unable to enter text in{xpath}")

    def click_by_javascript(self , xpath:str):
        try:
           element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
           self.driver.execute_script("arguments[0].click();", element)
        except:
             print(f"Unable to click {xpath}")

    def wait_for_element_to_appear(self , xpath:str , timeout:None = 10):
        try:
            WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        except:
            print(f"Unable to find element {xpath}")


