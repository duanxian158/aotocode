# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 17:31
# @Author  : wangna
# @FileName: imge_code.py
# @Software: PyCharm

from PIL import Image,ImageEnhance
import pytesseract  # 用于图片转文字
import re  # 用于正则
import logging
from Common.base_page import BasePage
class ImageCode(BasePage):

    def __init__(self, driver):
        self.driver = driver
    def get_pictures(self,locator,model=""):
        # 获取验证码
        # self.driver.find_element_by_xpath(self.img_code)
        try:
            self.wait_eleVisible(locator)
            # 全屏截图
            self.driver.save_screenshot("pictures.png")
            # 打开截图
            page_snap_obj = Image.open("pictures.png")
            # 验证码元素位置//img[@class='piccodebutn']
            img = self.get_element(locator)
            location = img.location
            size = img.size  # 获取验证码的大小参数
            left = location['x']
            top = location['y']
            right = left + size['width']
            bottom = top + size['height']
            image_obj = page_snap_obj.crop((left, top, right, bottom))  # 按照验证码的长宽，切割验证码
            # image_obj.show()  # 打开切割后的完整验证码
            # self.driver.close()  # 处理完验证码后关闭浏览器
            return image_obj
        except:
            # 捕获异常到日志中：
            logging.exception("{0}图形验证码获取失败".format(model))
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self.screenshot(model)
            # 抛出异常
            raise

    #获取图片
    def processiong_image(self,locator):
        # 3、打开截图，获取验证码位置，截取保存验证码
        # image_obj =Image.open(r"D://Python37//code//1.png")
        image_obj = self.get_pictures(locator)#获取验证码
        img = image_obj.convert('L')#转灰度
        pixdata = img.load()
        w, h = img.size
        threshold = 160  # 该阈值不适合所有验证码，具体阈值请根据验证码情况设置
        # 遍历所有像素，大于阈值的为黑色
        for y in range(h):
            for x in range(w):
                if pixdata[x, y] < threshold:
                    pixdata[x, y] = 0
                else:
                    pixdata[x, y] = 255

        return img
    #删除噪点
    def delete_spot(self,locator):
        images = self.processiong_image(locator)
        data = images.getdata()
        w, h = images.size
        black_point = 0
        for x in range(1, w - 1):
            for y in range(1, h - 1):
                mid_pixel = data[w * y + x]  # 中央像素点像素值
                if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
                    top_pixel = data[w * (y - 1) + x]
                    left_pixel = data[w * y + (x - 1)]
                    down_pixel = data[w * (y + 1) + x]
                    right_pixel = data[w * y + (x + 1)]
                    # 判断上下左右的黑色像素点总个数
                    if top_pixel < 10:
                        black_point += 1
                    if left_pixel < 10:
                        black_point += 1
                    if down_pixel < 10:
                        black_point += 1
                    if right_pixel < 10:
                        black_point += 1
                    if black_point < 1:
                        images.putpixel((x, y), 255)
                    black_point = 0
        # images.show()
        return images
    #去掉特殊字符，空格
    def image_str(self,locator):
        image = self.delete_spot(locator)
        result = pytesseract.image_to_string(image)#图片转文字
        resultj = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", result)
        # result_four = resultj[0:4]#只获取前4个字符
        return resultj