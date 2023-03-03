import time

from selenium import webdriver

from base.base_page import BasePage
from selenium.webdriver.common.by import By


class ControlCenterPage(BasePage):
    # 页面的元素
    controlCenter_loc = (By.LINK_TEXT, "管理中心")  # 管理中心按钮
    newApplication_loc = (By.CLASS_NAME, "new-panel")  # 创建新应用按钮
    inputAppName_loc = (By.XPATH, "//input[@placeholder='请输入应用名称']")  # 输入应用名称框
    inputFormName_loc = (By.XPATH, "//input[@placeholder='请输入表单名称']")  # 输入应用名称框
    chooseIconBox_loc = (By.CLASS_NAME, "selected-icon")  # 选择应用图标下拉框
    chooseAppIconRGB_loc = (By.CSS_SELECTOR, "[style='background: rgb(245, 156, 68);']")  # 选择应用图标颜色
    chooseFormIconRGB_loc = (By.CSS_SELECTOR, "[style='background: rgb(255, 142, 61);']")  # 选择表单图标颜色
    chooseIcon_loc = (By.CSS_SELECTOR, "[class='iconfont icon-leidalianjie']")  # 选择应用图标
    confirmButton_loc = (
    By.XPATH, "//*[@id='app']/section/section/main/div/div[2]/div/div/div[3]/div/button[2]")  # 新建自定义应用/表单确定
    paasApp_loc = (By.XPATH, f"//p[text()='']")
    closeButton_loc = (By.XPATH, "//span[text()='关闭']")
    closedAppTab_loc = (By.XPATH, "//div[text()='未开启应用']")
    paasAppSetting_loc = (By.CLASS_NAME, "mask-icon")  # 表单浮层设置按钮
    deleteApp_loc = (By.CLASS_NAME, "redColor")  # 删除应用按钮
    deleteAppButton_loc = (By.XPATH, "//span[text()='删除']")  # 确认删除按钮

    formTemplateBtn_loc = (By.XPATH, '//span[text()="表单模板"]')   # 表单模板按钮
    addFormBtn_loc = (By.XPATH, '//span[text()="新建表单"]')        # 新建自定义表单按钮

    deleteFormBtn_loc = (By.XPATH, '//span[text()="删除"]')        # 删除自定义表单按钮
    editFormBtn_loc = (By.XPATH, '//span[text()="编辑"]')         # 编辑自定义表单按钮
    deleteConfirmBtn_loc = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "]')   # 删除确认按钮

    tip_loc = (By.CLASS_NAME, 'el-message__content')    # 错误提示框
    paasName_none_loc = (By.CLASS_NAME, 'el-form-item__error')      # 请输入应用名称/颜色和图标
    paasForm_none_loc = (By.CLASS_NAME, 'el-message-box__errormsg')     # 请输入此表单完整名称

    selectPaasFormName_loc = (By.CLASS_NAME, 'left-list_item')    # 选中的自定义表单




    def __init__(self):
        super().__init__()
        time.sleep(1)
        self.click(ControlCenterPage.controlCenter_loc)
        time.sleep(1)

    # 页面的动作

    # 新建自定义应用
    def addPaasApp(self, paasName):
        # time.sleep(1)
        # self.click(ControlCenterPage.controlCenter_loc)
        # time.sleep(1)
        self.click(ControlCenterPage.newApplication_loc)
        time.sleep(1)
        self.send_keys(ControlCenterPage.inputAppName_loc, paasName)
        self.click(ControlCenterPage.chooseIconBox_loc)
        self.click(ControlCenterPage.chooseAppIconRGB_loc)
        self.click(ControlCenterPage.chooseIcon_loc)
        self.click(ControlCenterPage.confirmButton_loc)
        time.sleep(1)

    # 新建自定义应用(值为空)
    def addPaasApp_isnone(self):
        self.click(ControlCenterPage.newApplication_loc)
        time.sleep(1)
        self.click(ControlCenterPage.confirmButton_loc)
        time.sleep(1)

    # 关闭自定义应用
    def closePaasApp(self, paasName):
        # time.sleep(1)
        # self.click(ControlCenterPage.controlCenter_loc)
        # time.sleep(1)
        self.hold(paasName)
        self.click(ControlCenterPage.closeButton_loc)
        time.sleep(1)

    # 删除自定义应用
    def deletePaasApp(self, paasName):
        # time.sleep(1)
        # self.click(ControlCenterPage.controlCenter_loc)
        # time.sleep(1)
        self.click(ControlCenterPage.closedAppTab_loc)
        time.sleep(1)
        self.hold(paasName)
        self.click(ControlCenterPage.paasAppSetting_loc)
        time.sleep(1)
        self.click(ControlCenterPage.deleteApp_loc)
        self.send_keys(ControlCenterPage.inputAppName_loc, paasName)
        self.click(ControlCenterPage.deleteAppButton_loc)
        time.sleep(1)

    # 进入到自定义应用
    def enterPaasApp(self, paasName):
        self.click(ControlCenterPage.formTemplateBtn_loc)
        button_list = self.driver.find_elements(By.XPATH, f"//span[text()='{paasName}']")
        if len(button_list) > 0:
            self.driver.execute_script("arguments[0].click();", button_list[0])
        else:
            print('error')
            return

    # 新建自定义表单
    def addPaasForm(self, paasName, paasAppName):
        self.enterPaasApp(paasName)
        time.sleep(1)
        try:
            self.click(ControlCenterPage.addFormBtn_loc)
            time.sleep(1)
            self.send_keys(ControlCenterPage.inputFormName_loc, paasAppName)
            self.click(ControlCenterPage.chooseIconBox_loc)
            self.click(ControlCenterPage.chooseFormIconRGB_loc)
            self.click(ControlCenterPage.chooseIcon_loc)
            self.click(ControlCenterPage.confirmButton_loc)
            time.sleep(1)
        except Exception as e:
            print(f'error:{e}')

    # 新建自定义表单(值为空)
    def addPaasForm_isnone(self, paasName):
        self.enterPaasApp(paasName)
        try:
            self.click(ControlCenterPage.addFormBtn_loc)
            time.sleep(1)
            self.click(ControlCenterPage.confirmButton_loc)
            time.sleep(1)
        except Exception as e:
            print(f'error:{e}')

    # 删除自定义表单
    def deletePaasForm(self, paasName, paasFormName):
        self.enterPaasApp(paasName)
        try:
            time.sleep(1)
            # self.click(self.selectPaasFormName_loc)
            temp_paasFormName = self.get_value(self.selectPaasFormName_loc)
            self.click(self.deleteFormBtn_loc)
            self.locator_element_placeholder(temp_paasFormName).send_keys(paasFormName)
            time.sleep(1)
            element = self.locator_element(self.deleteConfirmBtn_loc)
            self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            print(f'error:{e}')

    # 编辑自定义表单
    def enterEditPaasForm(self):
        self.enterPaasApp(paasName='灰度测试')
        time.sleep(1)
        self.click(self.editFormBtn_loc)
        time.sleep(1)




    # 断言
    def assert_addPaas_over20(self):
        return self.get_value(self.tip_loc)

    def assert_addPaas_isnone(self):
        error_list = self.driver.find_elements(By.CLASS_NAME, 'el-form-item__error')
        if len(error_list) > 0:
            passName = error_list[0].text
            passIcon = error_list[1].text
            return passName, passIcon

    def assert_deletePassForm_iswrong(self):
        return self.get_value(self.paasForm_none_loc)