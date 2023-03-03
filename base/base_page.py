import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
import json


class BasePage:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.debugger_address = 'localhost:9222'
        self.driver = webdriver.Chrome(options=options)
        self.main_url = 'https://ptwebf.xbongbong.com.cn/#/app/home'

    def enter_test1(self):
        self.driver.get(self.main_url)

    # 设置元素路径
    def locator_element(self, loc):
        return self.driver.find_element(*loc)

    # 设置元素组路径
    def locator_elements(self, loc):
        return self.driver.find_elements(*loc)

    # 设置带p关键字的元素路径
    def locator_element_p(self, value):
        return self.driver.find_element(By.XPATH, f"//p[text()='{value}']")

    # 设置带span关键字的元素路径
    def locator_element_span(self, value):
        return self.driver.find_element(By.XPATH, f"//span[text()='{value}']")

    # 设置带placeholder关键字的元素路径
    def locator_element_placeholder(self, value):
        return self.driver.find_element(By.XPATH, f"//input[@placeholder='{value}']")

    # 设置基础字段元素路径
    def locator_element_basefield(self, basefield, loc):
        return basefield.find_element(*loc)

    # 设置值的关键字
    def send_keys(self, loc, value):
        self.locator_element(loc).send_keys(value)

    # 单击的关键字
    def click(self, loc):
        self.locator_element(loc).click()

    # 单击的关键字
    def click_basefield(self, basefield, loc):
        self.locator_element_basefield(basefield, loc).click()

    # 鼠标悬浮的关键字
    def hold(self, value):
        mouse = self.locator_element_p(value)
        ActionChains(self.driver).move_to_element(mouse).perform()  # 鼠标悬浮

    # 获取文本的值
    def get_value(self, loc):
        return self.locator_element(loc).text

    # 解决element click intercepted
    def execute_script(self, loc):
        self.driver.execute_script("arguments[0].click();", loc)