import time
from datetime import datetime

from base.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    # 页面的元素
    applicationBtn_loc = (By.XPATH, "//span[@title='我是天选']")
    formBtn_loc = (By.XPATH, "//span[text()='回测模版（勿动）']")

    input_list_loc = (By.XPATH, "//input[@type='text']")
    textarea_list_loc = (By.CLASS_NAME, "el-textarea__inner")

    addBtn_loc = (By.ID, "add")

    def test_demo(self):
        app_name = "我是天选"
        form_name = "回测模版（勿动）"
        self.enter_form(app_name, form_name)
        self.add_data()

    def get_application_name_loc(self, app_name):
        applicationBtn_loc = (By.XPATH, f"//span[@title='{app_name}']")
        return applicationBtn_loc

    def get_form_name_loc(self, form_name):
        formBtn_loc = (By.XPATH, f"//span[text()='{form_name}']")
        return formBtn_loc

    def enter_form(self, app_name, form_name):
        self.driver.get(self.main_url)
        time.sleep(1)

        applicationBtn_loc = self.get_application_name_loc(app_name)
        self.click(applicationBtn_loc)
        print(f"选择应用：{app_name}")

        formBtn_loc = self.get_form_name_loc(form_name)
        formBtn = self.locator_element(formBtn_loc)
        self.execute_script(formBtn)
        print(f"选择表单：{form_name}")

        time.sleep(1)

    def add_data(self):
        self.click(self.addBtn_loc)
        print("点击新建按钮")

        time_now = datetime.now.strftime('%Y-%m-%d %H:%M:%S')
        input_list = self.locator_elements(self.input_list_loc)
        textarea_list = self.locator_elements(self.textarea_list_loc)

        single_line_text_value = f"{time_now}单行文本测试"
        self.send_keys(input_list[0], single_line_text_value)
        print(f"单行文本：{single_line_text_value}")

        multiple_lines_text_value = f"{time_now}多行文本测试"
        self.send_keys(textarea_list[0], multiple_lines_text_value)
        print(f"多行文本：{multiple_lines_text_value}")


