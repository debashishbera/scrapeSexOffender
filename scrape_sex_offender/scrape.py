import json
import random
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .browser import BrowserActivities
from .locators import Locators      
from .homepage import HomePage  

# Configure logging
logging.basicConfig(level=logging.INFO)

class ScrapSexOffender:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.browser = BrowserActivities(self.driver)
        self.url = "https://sexoffender.dsp.delaware.gov/"
    
    def get_info_about(self, first_name: str, last_name: str, number_of_offenders: int = None) -> None:
        offenders_info = []

        #hitting the url
        self.driver.get(self.url)
        self.wait_for_page_to_load()
        #validating the captcha
        self.validate_captcha()
        
        #Searching the name, also validating the captcha if it appears
        homepage = HomePage(self.driver, self.browser)
        homepage.search_the_name(first_name, last_name)
        self.validate_captcha()
        
        #check if there are no result
        if not homepage.is_results_not_present():
            #if no
            logging.info("Getting info")
            offenders_info = self.get_info(number_of_offenders)
        else:
            #if yes
            logging.info("No results were found")

        #Saving the data in a JSON file
        self.save_to_json(offenders_info)
        self.driver.quit()
        if offenders_info:
             logging.info("Done, Please check data.json file")
        else:
             logging.info(f"There were no results found for{first_name}{last_name}")
        

    def save_to_json(self, data: list[dict]) -> None:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

    def validate_captcha(self) -> None:
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.captcha_div)))
            logging.info("Captcha Found, trying to validate")
            number = random.randint(1, 3)
            time.sleep(number)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.captcha_submit_button)))
            self.browser.click_by_javascript(Locators.captcha_submit_button)
            self.check_for_captcha_error()
        except Exception as e:
            logging.info("No captcha on screen or error occurred")
        
    def check_for_captcha_error(self) -> None:
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Locators.captcha_error_paragraph)))
            logging.warning("Captcha validation failed, refreshing...")
            self.driver.refresh()
            self.validate_captcha()
        except Exception:
            logging.info("Captcha validated successfully")

    def click_on_offender(self, index: int) -> None:
        locator = self.get_random_locator_out_of([
            f'({Locators.first_names})[{index}]',
            f'({Locators.last_names})[{index}]'
        ])
        self.browser.click_on(locator)

    def get_registration_info(self) -> dict:
        self.browser.wait_for_element_to_appear(Locators.label)
        labels = self.driver.find_elements(By.XPATH, Locators.label)
        info = {
            "name": f"{self.get_text_content(Locators.first_name)} {self.get_text_content(Locators.last_name)}"
        }
        for label in labels:
            value = label.find_element(By.XPATH, Locators.value).get_attribute("textContent")
            info[label.text.rstrip(':')] = value

        print(info)
        return info

    def get_text_content(self, xpath: str) -> str:
        return self.driver.find_element(By.XPATH, xpath).get_attribute("textContent")

    def get_info(self, number_of_offenders: int) -> list[dict]:
        offenders_info = []
        page_number = 1

        while True:
            self.wait_for_page_to_load()

            url = self.driver.current_url
            url_list = url.strip('/')
            if page_number>1:
                #import pdb; pdb.set_trace()
                assert int(url_list[-1]) == page_number
            time.sleep(3)
            per_page_offenders = len(self.driver.find_elements(By.XPATH, Locators.first_names))+ 1
            for ind in range(1, per_page_offenders):
                self.click_on_offender(ind)
                time.sleep(2)
                print("started for" , ind)
                self.validate_captcha()
                print("finished for" , ind)
                time.sleep(2)
                offender_info = self.get_registration_info()
                offenders_info.append(offender_info)
                self.driver.back()
                time.sleep(2)
                if number_of_offenders is not None and len(offenders_info) >= number_of_offenders:
                    logging.info(f"Retrieved {number_of_offenders} offenders info from results")
                    return offenders_info
            
            print("Last page:",self.is_last_page())
            if self.is_last_page():
                break

            
            self.browser.click_on(Locators.next_button)
            self.validate_captcha()
            time.sleep(1.5)
            page_number += 1
        
        return offenders_info

    def is_last_page(self) -> bool:
        try:
            self.driver.find_element(By.XPATH,Locators.disabled_next_button)
            print("Last page")
            return True
        except Exception:
            logging.info("Going to the next page")
            return False

    def wait_for_page_to_load(self) -> None:
        WebDriverWait(self.driver, 15).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    def get_random_locator_out_of(self, values: list) -> str:
        return random.choice(values)
