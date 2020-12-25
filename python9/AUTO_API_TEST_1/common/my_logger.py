#日志
#1：什么是日志呢？记录代码运行的信息
#2：为什么要有日志？方便查找定位问题
#3：日志分为几个级别
#debug info warning error critical
#4：什么时候用什么级别？--实践里面讲
#python logging 自带的日志系统
#定义级别
#可以输出到控制台还是指定的文件  输出渠道的限制
import logging
from common import pro_path
# 控制日志输出格式
formatter='%(asctime)s-%(levelname)s-%(filename)s-日志信息:%(message)s'
# 日期格式
dfmt='%a, %d %b %Y %H:%M:%S'
#添加到文件
fh=logging.FileHandler(pro_path.test_log_path,encoding='UTF-8')
sh=logging.StreamHandler()#到控制台
logging.basicConfig(level=logging.DEBUG,handlers=[fh,sh],format=formatter,datefmt=dfmt)
# logging.debug('这是一个debug级别的信息')
# logging.info('这是一个info级别的信息') #只想记录信息 用.info
# logging.warning('这是一个warning级别的信息')
# logging.error('这是一个error级别的信息') #记录错误信息  用.error  如异常处理
# logging.critical('这是一个critical级别的信息')


