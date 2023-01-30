from typing import List

from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from earap.scraping.StepClass import Step


class Driver():
    def __init__(self, url: str):
        chrome_service = fs.Service(executable_path='./chromedriver.exe')
        browser = webdriver.Chrome(service=chrome_service)
        self.browser = browser
        self.browser.get(url)

    def end(self):
        self.browser.close()

    def check_robots_text():
        pass

    def select_xpath(self, xpath: str):
        return self.browser.find_element(By.XPATH, xpath)

    def click_link(self, xpath: str):
        elem = self.select_xpath(xpath)
        elem.click()

    def click_enter(self, xpath: str):
        elem = self.select_xpath(xpath)
        elem.send_keys(Keys.ENTER)

    def insert_data(self, xpath: str, content: str):
        elem = self.select_xpath(xpath)
        elem.send_keys(content)

    def insert_and_enter(self, xpath: str, content: str):
        elem = self.select_xpath(xpath)
        elem.send_keys(content)
        elem.send_keys(Keys.ENTER)

    def sort_steps(self, steps: List[Step]):
        return steps

    def chain_steps(self, steps: List[Step]):
        sorted_steps = self.sort_steps(steps)
        for step in sorted_steps:
            if step['action'] == 'click':
                self.click_link(step['xpath'])
            elif step['action'] == 'insert':
                self.insert_data(step['xpath'], step['value'])
            elif step['action'] == 'insert_and_enter':
                self.insert_and_enter(step['xpath'], step['value'])
            else:
                pass
        # 3秒待機
        time.sleep(10)
