import random
import time
import datetime

from base.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    # 页面的元素
    input_list_loc = (By.XPATH, "//input[@type='text']")
    textarea_list_loc = (By.CLASS_NAME, "el-textarea__inner")
    date_tree_list_loc = (By.CLASS_NAME, "el-date-table__row")
    date_list_loc = (By.CLASS_NAME, "el-date-picker__header-label")
    radio_list_loc = (By.CLASS_NAME, "el-radio__label")
    checkbox_list_loc = (By.CLASS_NAME, "el-checkbox__label")

    addBtn_loc = (By.ID, "add")
    saveBtn_loc = (By.XPATH, "//*[@id='app']/div[1]/div/div/div[1]/div/div[3]/button[2]")

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
        self.wait()

        applicationBtn_loc = self.get_application_name_loc(app_name)
        self.click(applicationBtn_loc)
        print(f"选择应用：{app_name}")
        self.wait()

        formBtn_loc = self.get_form_name_loc(form_name)
        formBtn = self.locator_element(formBtn_loc)
        self.execute_script(formBtn)
        print(f"选择表单：{form_name}")
        self.wait()

    def add_data(self):
        self.click(self.addBtn_loc)
        print("点击新建按钮")
        self.wait()

        time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        input_list = self.locator_elements(self.input_list_loc)
        textarea_list = self.locator_elements(self.textarea_list_loc)

        # 输入单行文本值
        single_line_text_value = f"{time_now}单行文本测试"
        single_line_text_input = input_list[4]
        single_line_text_input.send_keys(single_line_text_value)
        print(f"单行文本：{single_line_text_value}")

        # 输入多行文本值
        multiple_lines_text_value = f"{time_now}多行文本测试"
        multiple_lines_text_input = textarea_list[0]
        multiple_lines_text_input.send_keys(multiple_lines_text_value)
        print(f"多行文本：{multiple_lines_text_value}")

        # 输入数字
        number_value = random.randint(0, 1000)
        number_input = input_list[5]
        number_input.send_keys(number_value)
        print(f"数字：{number_value}")

        # 输入日期
        date_spinner = input_list[6]
        date_spinner.click()

        date_tr_list = self.locator_elements(self.date_tree_list_loc)
        date_tr = date_tr_list[random.randint(0, len(date_tr_list) - 1)]

        date_td_list = date_tr.find_elements(By.XPATH, ".//td")
        date_td = date_td_list[random.randint(0, len(date_td_list) - 1)]
        date_day = f"{date_td.text}日"
        date_td.click()

        date_spinner.click()
        date_list = self.locator_elements(self.date_list_loc)
        date_year = date_list[0].text.replace(" ", "")
        date_month = date_list[1].text.replace(" ", "")
        print(f"日期：{date_year}{date_month}{date_day}")

        # 单击单行文本框取消聚焦
        single_line_text_input.click()

        # 选择单选按钮
        radio_list = self.locator_elements(self.radio_list_loc)
        radio = radio_list[random.randint(0, len(radio_list)-1)]
        radio.click()
        radio_color = radio.find_element(By.XPATH, ".//span").get_attribute("style")
        radio_value = radio.text
        print(f"单选按钮值：{radio_value}，颜色：{radio_color}")
        # todo 输入其他值

        # 选择复选框组
        checkbox_list = self.locator_elements(self.checkbox_list_loc)
        checkbox_chosen_count = random.randint(0, len(checkbox_list))
        checkbox_chosen_list = random.sample(checkbox_list,checkbox_chosen_count)
        print(checkbox_chosen_list)
        for i in checkbox_chosen_list:
            i.click()

        self.wait()
        self.click(self.saveBtn_loc)
