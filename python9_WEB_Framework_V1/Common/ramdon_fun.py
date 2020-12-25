# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 15:31
# @Author  : wangna
# @FileName: ramdon_phone.py
import random,string
import logging
import string
class RamdonFun:
    #手机号11位
    def create_phone(self):
        # 第二位数字
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]

        # 第三位数字
        third = {
            3: random.randint(0, 9),
            4: [5, 7, 9][random.randint(0, 2)],
            5: [i for i in range(10) if i != 4][random.randint(0, 8)],
            7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
            8: random.randint(0, 9),
        }[second]

        # 最后八位数字
        suffix = random.randint(9999999, 100000000)
        logging.info("随机生成手机号：1{0}{1}{2}".format(second, third, suffix))
        # 拼接手机号
        return "1{0}{1}{2}".format(second, third, suffix)

    #随机数 从a-zA-Z0-9生成指定数量的随机字符
    def ramdom_num(self,length):
        value = ''.join(random.sample(string.ascii_letters + string.digits, length))
        return value
if __name__ == '__main__':
    phone = RamdonFun().ramdom_num(3)
    print(phone)