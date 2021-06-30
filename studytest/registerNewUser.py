# coding=utf-8
import unittest
from selenium import webdriver


class RegisterNewUser(unittest.TestCase):
    u"""注册"""

    @classmethod
    def setUpClass(cls):  # cls : 表示没有被实例化的类本身
        # edge浏览器使用绝对路径
        driver_url = r"C:\driver\msedgedriver.exe"
        cls.driver = webdriver.Edge(executable_path=driver_url)
        cls.driver.get("https://mail.163.com/")
        # 智能等待
        cls.driver.implicitly_wait(30)
        # 最大化浏览器
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        # 退出并关闭窗口的每一个相关的驱动程序，有洁癖用这个
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
