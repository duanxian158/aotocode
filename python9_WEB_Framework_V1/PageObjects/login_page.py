# -*- coding: utf-8 -*-
# @Time    : 2020/11/7 14:32
# @Author  : wangna
# @FileName: login_page.py
# @Software: PyCharm
from PageLocators.login_page_locator import LoginPageLocator
from Common.base_page import BasePage
from Common.imge_code import ImageCode
import time
#页面对象，操作元素，继承元素类
class LoginPage(LoginPageLocator,BasePage):

    def __init__(self,driver):
        self.driver=driver
        # 获取图睛

    # def get_pictures(self):
    #     # 获取验证码
    #     # self.driver.find_element_by_xpath(self.img_code)
    #     name = "登录功能-获取验证码元素"
    #     self.wait_eleVisible(self.img_code,model=name)
    #     # 全屏截图
    #     self.driver.save_screenshot("pictures.png")
    #     # 打开截图
    #     page_snap_obj = Image.open("pictures.png")
    #     # 验证码元素位置//img[@class='piccodebutn']
    #     img = self.get_element(self.img_code)
    #     location = img.location
    #     size = img.size  # 获取验证码的大小参数
    #     left = location['x']
    #     top = location['y']
    #     right = left + size['width']
    #     bottom = top + size['height']
    #     image_obj = page_snap_obj.crop((left, top, right, bottom))  # 按照验证码的长宽，切割验证码
    #     # image_obj.show()  # 打开切割后的完整验证码
    #     # self.driver.close()  # 处理完验证码后关闭浏览器
    #     return image_obj

    def login(self,username,passwd):
        #日志内容：登录页面的登录功能
        name = "登录页面_登录功能"
        #企业登录输入手机号
        self.wait_eleVisible(self.user_input,model=name)
        self.input_text(self.user_input,username,model=name)
        #获取验证码
        image = ImageCode(self.driver).image_str(self.img_code)
        #输入验证码
        self.input_text(self.piccode_input,image,model=name)
        #输入密码
        self.input_text(self.passwd_input,passwd,model=name)
        #点击登录
        self.click_element(self.login_button,model=name)
    #获取错误信息
    def get_errorMsg_fromLoginArea(self):
        name="登录页面_登录区域错误提示"
        return self.get_text(self.error_prompt_fromLoginArea,model=name)
    def register(self):
        pass