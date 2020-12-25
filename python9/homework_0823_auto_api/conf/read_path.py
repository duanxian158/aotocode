from homework_0823.common.read_config import ReadConfig
import os
# #获取配置文件绝对路径 取当前路径 -》截取-》拼接
# s=os.path.split(os.path.realpath(__file__))[0]
# print(s)
conf_path=os.path.join(os.path.split(os.path.realpath(__file__))[0],'pro.conf')
# print(conf_path)
pro_path=ReadConfig().read_config(conf_path,'PRO_PATH','pro_path')
# excel_path=pro_path+'\\test_data\\test_1.xlsx'#第一种拼接
#第二种拼接 根据join拼接  导入import os
test_data_path=os.path.join(pro_path,'test_data','test_1.xlsx')#获取文件路径
# print(test_data_path)
report_path=os.path.join(pro_path,'test_report','test_report.html')
# print(report_path)
#作业题：
#路径中怎么实现自动修改配置文件里面的项目路径，不用每次去手动变更