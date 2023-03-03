import time

from base.base_page import BasePage
from selenium.webdriver.common.by import By


class Login(BasePage):
    # 页面的元素
    loginDingdingAccountBtn_loc = (By.XPATH, "//a[text()='登录钉钉账号']")
    phoneInput_loc = (By.ID, "mobile")
    passwordInput_loc = (By.ID, "pwd")
    confirmLoginBtn_loc = (By.ID, "loginBtn")
    ceshiMisaki_loc = (By.XPATH, "/html/body/div/div/ul/li[2]")
    loginBtn_loc = (By.CLASS_NAME, "button")

    QR_url = 'https://oapi.dingtalk.com/connect/oauth2/sns_authorize?appid=dingoaeutgeqqo2unmguzl' \
             '&response_type=code&scope=snsapi_login&state=STATE&redirect_uri=https://testdingtalkapi' \
             '.xbongbong.com.cn/pro/scan-code.html'

    def login(self):
        self.driver.get(self.QR_url)
        self.click(self.loginDingdingAccountBtn_loc)
        self.input_userdata()
        self.choose_company()
        self.confirm_login()

    def input_userdata(self):
        phone_number = "17606745824"
        password = "ColayKD41"
        self.send_keys(self.phoneInput_loc, phone_number)
        self.send_keys(self.passwordInput_loc, password)
        self.click(self.confirmLoginBtn_loc)
        print(f"账号：{phone_number}，选择公司中")
        self.wait()

    def choose_company(self):
        self.click(self.ceshiMisaki_loc)
        print("选择公司：测试misaki")

    def confirm_login(self):
        self.click(self.loginBtn_loc)
        self.wait()
        print("登陆成功")
