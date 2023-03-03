import os
import time
from PIL import Image

import zxing
from selenium import webdriver
from selenium.webdriver.common.by import By


def QR_code_login():
    driver = webdriver.Chrome()
    main_url = 'https://ptwebf.xbongbong.com.cn/login.html'
    driver.get(main_url)
    time.sleep(3)
    f = driver.find_element(By.XPATH, '/html/body/div[1]/iframe')
    driver.switch_to.frame(f)
    iframe = driver.find_element(By.XPATH, '//*[@id="code-container"]/iframe')
    driver.switch_to.frame(iframe)
    image_driver = driver.find_element(By.XPATH, '//*[@id="qrcode"]/img')
    path = os.getcwd() + '/Qr_code.png'  # 图片路径
    image_driver.screenshot(path)  # 保存图片
    img = Image.open(path)
    img.save(path)
    zx = zxing.BarCodeReader()  # 调用zxing二维码读取包
    QR_code_info = zx.decode(path)  # 图片解码
    code = str(QR_code_info).split("'")
    os.remove(path)
    print(code)
    # ws_driver = get_ws_driver('api url')  # 我用的websocket 开启websocket cline
    # sid = (login(ws_driver, 手机号, 密码))['data']['sid']  # 得到sid
    # ws_rq_login_for_app(ws_driver, qr_sid=code[1], sid=sid, project_id=1, team_id=1)  # 调用qr_login api 输入参数等
    # sleep(20)
    # driver.close()
    # return code[1]  # 返回记录的内容


if __name__ == '__main__':
    QR_code_login()
