# coding=utf-8

import sys
# print(sys.path)
#
sys.path.append("C:\\Users\\chenzhimei\\PycharmProjects\\SeleniumPython")
sys.path.append("C:\\Program Files\\JetBrains\\PyCharm 2020.2.3\\plugins\\python\\helpers\\pycharm_display")
sys.path.append("C:\\Users\\chenzhimei\\AppData\\Local\\Programs\\Python\\Python39\\python39.zip")
sys.path.append("C:\\Users\\chenzhimei\\AppData\\Local\\Programs\\Python\\Python39\\DLLs")
sys.path.append("C:\\Users\\chenzhimei\\AppData\\Local\\Programs\\Python\\Python39\\lib")
sys.path.append("C:\\Users\\chenzhimei\\AppData\\Local\\Programs\\Python\\Python39")
sys.path.append("C:\\Users\\chenzhimei\\PycharmProjects\\SeleniumPython\\venv")
sys.path.append("C:\\Users\\chenzhimei\\PycharmProjects\\SeleniumPython\\venv\\lib\\site-packages")
sys.path.append("C:\\Program Files\\JetBrains\\PyCharm 2020.2.3\\plugins\\python\\helpers\\pycharm_matplotlib_backend")

import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb18030")

import unittest
from xmlrunner import xmlrunner
import HTMLTestRunner
import os
from studytest.start_browser import Login
from studytest.HomePage import HomePageTest


# 获取当前路径，存测试报告
current_path = os.getcwd()

# 取到所有的测试用例
# TestLoader类，可以得到指定的测试文件中的测试方法且用于测试套件
login_tests = unittest.TestLoader().loadTestsFromTestCase(Login)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# 创建一个测试套件（TestSuite）
smoke_tests = unittest.TestSuite([home_page_tests, login_tests])

# 执行测试套件TextTestRunner
# unittest.TextTestRunner(verbosity=2).run(smoke_tests)

# 打开文件
outfile = open(current_path + "\SomkeTestReport.html", 'wb')

'''
No module named HTMLTestRunner，查了一下HTMLTestRunner是unittest测试框架的一个扩展，需要下载下来放到python安装目录的Lib下面即可。
下载连接http://tungwaiyip.info/software/HTMLTestRunner.html，打开连接后右键点击HTMLTestRunner.py另存为即可。
'''
runner = HTMLTestRunner.HTMLTestRunner(
    stream=outfile,
    title='测试报告',
    description='冒烟测试'
)

# 执行测试套件用HTMLTestRunner
# runner.run(smoke_tests)
'''
# 执行后，若报错ModuleNotFoundError: No module name 'StringIO'
因为下载的HTMLTestRunner是Python2版本的，Python3的话要修改一下：
第94行，将import StringIO修改成import io
第539行，将self.outputBuffer = StringIO.StringIO()修改成self.outputBuffer= io.StringIO()
第642行，将if not rmap.has_key(cls):修改成if not cls in rmap:
第766行，将uo = o.decode(‘latin-1‘)修改成uo = e
第775行，将ue = e.decode(‘latin-1‘)修改成ue = e
第631行，将print >> sys.stderr, ‘\nTime Elapsed: %s‘ %(self.stopTime-self.startTime)
修改成print(sys.stderr, '\nTimeElapsed: %s' % (self.stopTime-self.startTime))
'''

# 执行测试套件用XMLrunner
xmlrunner.XMLTestRunner(verbosity=2, output='测试报告').run(smoke_tests)



# 411e441dc84145a2a105b32ec0d406b3