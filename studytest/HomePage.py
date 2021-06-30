# coding=utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class HomePageTest(unittest.TestCase):
    # 类方法（不需要实例化类就可以被类本身调用）
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

    def test_search_text(self):
        u"""element.text方法"""
        driver = self.driver
        # 操作测试对象
        '''
        一般来说，webdriver 中比较常用的操作对象的方法有下面几个
         click 点击对象
         send_keys 在对象上模拟按键输入
         clear 清除对象的内容，如果可以的话
         submit 提交表单   把“百度一下”的操作从 click 换成 submit 可以达到相同的效果
         text 用于获取元素的文本信息
        '''
        data = driver.find_element_by_xpath('//*[@id="footer"]/div/div[2]/span[1]').text
        print(data)
        self.assertEqual("网易公司版权所有©1997-2021",data)

    def test_register_is_present(self):
        u"""ink text定位，注册网易邮箱是否存在"""
        # link text位
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "注册网易邮箱"))

    def test_csslocate(self):
        u"""CSS定位练习"""
        driver = self.driver
        # css定位
        # http://www.w3.org/TR/css3-selectors/
        # http://www.w3school.com.cn/css/css_positioning.asp
        # 定位
        css_element = driver.find_element_by_css_selector("p.headerTitle").text
        self.assertEqual("中文邮箱第一品牌",css_element)

        # wang = driver.find_element_by_css_selector("div.header > div.headerLogo > p").text
        # print(wang)
        # # self.assertEqual("163网易邮箱",wang)

    def test_youxiang_is_present(self):
        u"""右上角“163网易免费邮"图片是否存在"""
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"div.headerLogo p"))

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        # 退出并关闭窗口的每一个相关的驱动程序，有洁癖用这个
        cls.driver.quit()
        # 关闭当前窗口
        # self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
