import datetime
import time
import unittest
import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
import json
import warnings

from base.base_page import BasePage
from pageobject.ControlCenter_page import ControlCenterPage
from BeautifulReport import BeautifulReport

from pageobject.FormDesign_page import FormDesign
from pageobject.Login_page import Login
from pageobject.Main_page import MainPage


class TestCase(unittest.TestCase):

    # def setUp(self, ) -> None:
    #     print("setUp")
    #
    # def tearDown(self) -> None:
    #     try:
    #         print("tearDown")
    #     except ConnectionAbortedError as e:
    #         print(e)

    @classmethod
    def setUpClass(cls) -> None:
        warnings.simplefilter('ignore', ResourceWarning)

    def test_01_login(self):
        print("test_01_login")
        lg = Login()
        self.driver = lg.login()
        time.sleep(5)

    def test_02_mainpage(self):
        print("test_02_mainpage")
        mp = MainPage()
        mp.test_demo()
        time.sleep(5)
