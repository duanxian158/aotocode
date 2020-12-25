# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 10:27
# @Author  : wangna
# @FileName: BasePage.py
# @Software: PyCharm
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from Common import logger
from Common.dir_config import screenshot_dir
import time
import logging
from PIL import Image
class BasePage:
    def __init__(self,driver):
        self.driver=driver

    #等待元素可见-失败的时修改有截图有日志
    def wait_eleVisible(self,locator,wait_times=15,poll_requency=0.5,model = ""):
        """
        :param locator: 类型为元组(By.xxx,定位表达式)
        :return:
        """
        try:
            #开始时间
            start_time = time.time()
            WebDriverWait(self.driver, wait_times,poll_requency).until(
                EC.visibility_of_element_located(locator))
            #结束时间-求差值，转换成单人闰秒。写入日志。
            end_time = time.time()

            # logging.info("{0},{1},{2}".format("元素可见成功：",model,locator))
        except:

            #捕获异常到日志中：
            logging.exception("{0},{1},{2}".format("等待元素可见失败：",model,locator))
            #截图 - 保存到的指定的目录。名字要想好怎么取？
            self.screenshot(model)
            #抛出异常
            raise

    #查找元素
    def get_element(self,locator,model = ""):
        #
        try:
            return self.driver.find_element(locator[0],locator[1])
        except:
            # 捕获异常到日志中：
            logging.exception("{0},{1},{2}".format("未找到元素:",model,locator))
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self.screenshot(model)
            # 抛出异常
            raise
    #输入操作
    def input_text(self,locator,text,model = ""):
        #找到元素
        ele = self.get_element(locator)
        #输入操作
        try:
            ele.send_keys(text)
        except:
            # 捕获异常到日志中：
            logging.exception("输入操作失败：{0},{1}".format(model,locator))
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self.screenshot(model)
            # 抛出异常
            raise
    #点击操作
    def click_element(self,locator,model = ""):
        #找到元素
        ele = self.get_element(locator)
        #点击操作
        try:
            ele.click()
            # logging.info("点击成功：{0},{1}".format(model,locator))
        except:
            # 捕获异常到日志中：
            logging.exception("点击操作失败：{0}{1}".format(model,locator))
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self.screenshot(model)
            # 抛出异常
            raise
    #获取元素的属性

    #获取元素的文本
    def get_text(self,locator,model=""):
        #找到元素
        ele = self.get_element(locator)
        try:
            #返回元素的文本
            return ele.text
        except:
            # 捕获异常到日志中：
            logging.exception("{0}点击操作失败{1}".format(model,locator))
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self.screenshot(model)
            # 抛出异常
            raise


    #截图函数
    def screenshot(self,model):
        #时间
        filePah = screenshot_dir+"/{0}_{1}.png".format(model,time.strftime("%Y%m%d_%H%M%S"))
        self.driver.save_screenshot(filePah)
        logging.info("截图成功，图片路径为： {0}".format(filePah))

    #多窗口切换
    def get_window_handel(self):
        """
        切换到当前窗口
        :return:
        """
        handles = self.driver.window_handles
        # handle = self.drvier.current_window_handle  # 获取当前页的标签页的窗口句柄
        # self.driver.switch_to.window(self.driver.window_handles[-1])#切换到最新的窗口句柄
        logging.info("所有句丙{0}".format(handles))
        # logging.info("当前句柄{0}".format(self.driver.current_window_handle))
        self.driver.switch_to.window(handles[-1])
    #
    #     # 等待新的窗口出现-失败的时修改有截图有日志
    #
    # def wait_windowsVisible(self, curhandle, wait_times=15, poll_requency=0.5, model=""):
    #     """
    #     :param locator: 类型为元组(By.xxx,定位表达式)
    #     :return:
    #     """
    #     try:
    #         # 开始时间
    #         start_time = time.time()
    #         WebDriverWait(self.driver, wait_times, poll_requency).until(
    #             EC.new_window_is_opened(curhandle))
    #         # 结束时间-求差值，转换成单人闰秒。写入日志。
    #         end_time = time.time()
    #
    #         logging.info("{0},{1},{2}".format("窗口出现成功：", model, curhandle))
    #     except:
    #
    #         # 捕获异常到日志中：
    #         logging.exception("{0},{1},{2}".format("窗口出现失败：", model, curhandle))
    #         # 截图 - 保存到的指定的目录。名字要想好怎么取？
    #         self.screenshot(model)
    #         # 抛出异常
    #         raise
