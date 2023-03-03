import time

from base.base_page import BasePage
from selenium.webdriver.common.by import By

class FormDesign(BasePage):
    # 页面的元素
    # saveBtn_loc = (By.XPATH, '//span[text()="保存"]')     # 保存按钮(生产定位不到)
    saveBtn_loc = (By.XPATH, '//*[@id="app"]/section/section/main/div/section/main/div[1]/div[1]/button[2]')    # 保存按钮
    previewBtn_loc = (By.XPATH, '//span[text()="预览"]')  # 预览按钮

    # 基础字段(Base Field)
    basefield_loc = (By.XPATH, '//div[@class="field-group--base"]')
    text_bf_loc = (By.XPATH, '//span[text()="单行文本"]')     # 单行文本
    textarea_bf_loc = (By.XPATH, '//span[text()="多行文本"]')  # 多行文本
    number_bf_loc = (By.XPATH, '//span[text()="数字"]')  # 数字
    date_bf_loc = (By.XPATH, '//span[text()="日期"]')  # 日期
    radio_bf_loc = (By.XPATH, '//span[text()="单选按钮"]')  # 单选按钮
    checkbox_bf_loc = (By.XPATH, '//span[text()="复选框组"]')  # 复选框组
    dropdown_bf_loc = (By.XPATH, '//span[text()="下拉框"]')  # 下拉框
    multiselect_bf_loc = (By.XPATH, '//span[text()="下拉复选框"]')  # 下拉复选框
    separator_bf_loc = (By.XPATH, '//span[text()="分割线"]')  # 分割线
    address_bf_loc = (By.XPATH, '//span[text()="地址"]')  # 地址
    location_bf_loc = (By.XPATH, '//span[text()="定位"]')  # 定位
    image_bf_loc = (By.XPATH, '//span[text()="图片"]')  # 图片
    attachment_bf_loc = (By.XPATH, '//span[text()="附件"]')  # 附件
    description_bf_loc = (By.XPATH, '//span[text()="描述文本"]')  # 描述文本
    tags_bf_loc = (By.XPATH, '//span[text()="标签"]')  # 标签

    fieldAttribute_loc = (By.CLASS_NAME, 'el-tabs__content')    # 字段属性按钮
    deleteBtn_loc = (By.XPATH, '//button[@title="删除"]')   # 删除按钮
    attr_type_loc = (By.CLASS_NAME, 'attr-type')    # 字段类型

    # 添加基本字段
    def addBaseField(self):
        basefield = self.locator_element(self.basefield_loc)
        self.click_basefield(basefield, self.text_bf_loc)
        self.setTextAttriubtion()
        self.click_basefield(basefield, self.textarea_bf_loc)
        self.setTextareaAttriubtion()
        # self.click_basefield(basefield, self.number_bf_loc)
        # self.click_basefield(basefield, self.date_bf_loc)
        # self.click_basefield(basefield, self.radio_bf_loc)
        # self.click_basefield(basefield, self.checkbox_bf_loc)
        # self.click_basefield(basefield, self.dropdown_bf_loc)
        # self.click_basefield(basefield, self.multiselect_bf_loc)
        # self.click_basefield(basefield, self.separator_bf_loc)
        # self.click_basefield(basefield, self.address_bf_loc)
        # self.click_basefield(basefield, self.location_bf_loc)
        # self.click_basefield(basefield, self.image_bf_loc)
        # self.click_basefield(basefield, self.attachment_bf_loc)
        # self.click_basefield(basefield, self.description_bf_loc)
        # self.click_basefield(basefield, self.tags_bf_loc)
        time.sleep(1)
        # self.click(self.saveBtn_loc)
        self.click(self.previewBtn_loc)

    # 选取字段属性的元素
    def selectFieldAttribute(self, attr):
        attribute = ()
        placeholder = ''
        match attr:
            case '标题':
                placeholder = '请输入内容'
                attribute = (By.XPATH, f'//input[@placeholder="{placeholder}"]')
            case '描述信息':
                placeholder = '请输入描述信息'
                attribute = (By.XPATH, f'//textarea[@placeholder="{placeholder}"]')
            case '单行文本默认值':
                placeholder = '请输入默认值'
                attribute = (By.XPATH, f'//input[@placeholder="{placeholder}"]')
            case '多行文本默认值':
                placeholder = '请输入默认值'
                attribute = (By.XPATH, f'//textarea[@placeholder="{placeholder}"]')
            case '字段类型':
                placeholder = '请选择'
                attribute = (By.XPATH, f'//input[@placeholder="{placeholder}"]')
        return attribute

    # 设置单行文本属性
    def setTextAttriubtion(self):
        self.locator_element(self.selectFieldAttribute('标题')).clear()
        self.send_keys(self.selectFieldAttribute('标题'), '古诗词')
        self.send_keys(self.selectFieldAttribute('描述信息'), '古诗词')
        self.send_keys(self.selectFieldAttribute('单行文本默认值'), '赤壁赋')
        time.sleep(1)
        # self.click(self.attr_type_loc)

    def setTextareaAttriubtion(self):
        self.locator_element(self.selectFieldAttribute('标题')).clear()
        self.send_keys(self.selectFieldAttribute('标题'), '古诗词')
        self.send_keys(self.selectFieldAttribute('描述信息'), '古诗词')
        self.send_keys(self.selectFieldAttribute('多行文本默认值'), '壬戌之秋，七月既望，苏子与客泛舟游于赤壁之下。清风徐来，水波不兴。举酒属客，诵明月之诗，歌窈窕之章。少焉，月出于东山之上，徘徊于斗牛之间。白露横江，水光接天。纵一苇之所如，凌万顷之茫然。浩浩乎如冯虚御风，而不知其所止；飘飘乎如遗世独立，羽化而登仙。于是饮酒乐甚，扣舷而歌之。歌曰：“桂棹兮兰桨，击空明兮溯流光。渺渺兮予怀，望美人兮天一方。”客有吹洞箫者，倚歌而和之。其声呜呜然，如怨如慕，如泣如诉，余音袅袅，不绝如缕。舞幽壑之潜蛟，泣孤舟之嫠妇。苏子愀然，正襟危坐而问客曰：“何为其然也？”客曰：“月明星稀，乌鹊南飞，此非曹孟德之诗乎？西望夏口，东望武昌，山川相缪，郁乎苍苍，此非孟德之困于周郎者乎？方其破荆州，下江陵，顺流而东也，舳舻千里，旌旗蔽空，酾酒临江，横槊赋诗，固一世之雄也，而今安在哉？况吾与子渔樵于江渚之上，侣鱼虾而友麋鹿，驾一叶之扁舟，举匏樽以相属。寄蜉蝣于天地，渺沧海之一粟。哀吾生之须臾，羡长江之无穷。挟飞仙以遨游，抱明月而长终。知不可乎骤得，托遗响于悲风。”苏子曰：“客亦知夫水与月乎？逝者如斯，而未尝往也；盈虚者如彼，而卒莫消长也。盖将自其变者而观之，则天地曾不能以一瞬；自其不变者而观之')


    def deleteBtn_click(self, num):
        delete_list = self.driver.find_elements(*self.deleteBtn_loc)
        if len(delete_list) > 0:
            delete_list[num].click()