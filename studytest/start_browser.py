# coding=utf-8
# import time
import unittest
from selenium import webdriver


# from selenium.webdriver.support import expected_conditions as EC


class Login(unittest.TestCase):
    # 类方法（不需要实例化类就可以被类本身调用）
    # 这样 同一个测试中，不同测试用例只调用一次
    @classmethod
    def setUpClass(cls):  # cls : 表示没有被实例化的类本身
        # chrome使用相对路径就好
        # self.driver = webdriver.Chrome()
        # self.driver.get("http://baidu.com")

        # edge浏览器使用绝对路径
        # 驱动下载地址：https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
        driver_url = r"C:\driver\msedgedriver.exe"
        cls.driver = webdriver.Edge(executable_path=driver_url)
        cls.driver.get("https://mail.163.com/")
        # self.driver.get("https://www.baidu.com/")

        # 浏览器常用操作
        # 设置浏览框宽、高
        # self.driver.set_window_size(480, 800)

        # 添加等待时间，5秒
        # time.sleep(5)
        # 智能等待
        # implicitly_wait(30)的用法应该比 time.sleep() 更智能，后者只能选择一个固定的时间的等待，前者可以在一个时间范围内智能的等待。
        cls.driver.implicitly_wait(30)
        # 最大化浏览器
        cls.driver.maximize_window()

    def test_Login(self):
        driver = self.driver
        # 定位
        # 百度搜索框定位
        # id定位，如百度搜索框 input控件的id是固定值，即可以使用，一般也是唯一的；若id不指定，自动生成，那么就不适用了；name定位类似
        # send_keys方法往框中输入值 ;click点击
        # driver.find_element_by_id("kw").send_keys("Mayvay")
        # driver.find_element_by_id("su").click()
        # driver.find_element_by_name("wd").send_keys("Mayvay")

        # 163免费邮
        # link 有时候不是一个输入框也不是一个按钮，而是一个文字链接，我们可以通过 link
        # 一般一个页面上不会出现相同的文件链接，通过文字链接来定位也是一种简单有效的定位方式
        # driver.find_element_by_link_text("登录反馈").click()

        # Partial link text 定位. 可以只用链接的一部分文字进行匹配
        # driver.find_element_by_partial_link_text("反馈").click()

        # 163免费邮登录界面 由多层框架iframe,且iframe拼接了动态ID
        # switch_to_frame()定位框架iframe
        '''
        遇到动态Id可以利用xpath等元素属性来定位，下面列举xpath中提供的三个非常好的方法：
        1.contains(a, b) 如果a中含有字符串b，则返回true，否则返回false
        　　driver.find_element_by_xpath("//div[contains(@id, 'btn-attention')]")
        2.starts-with(a, b) 如果a是以字符串b开头，返回true，否则返回false
        　　driver.find_element_by_xpath("//div[starts-with(@id, 'btn-attention')]")
        3.ends-with(a, b) 如果a是以字符串b结尾，返回true，否则返回false
        　　driver.find_element_by_xpath("//div[ends-with(@id, 'btn-attention')]") 
        '''
        iframe = driver.find_element_by_xpath('//*[@id="loginDiv"]/iframe')  # 使用Xpath选定位到iframe
        driver.switch_to.frame(iframe)  # 定位切换到iframe
        # # iframe = driver.find_element_by_xpath("//iframe[contains(@id, 'x-URS-iframe')]")  # 使用Xpath提供的contains定位
        # # driver.switch_to.frame(iframe)
        # name定位
        driver.find_element_by_name('email').send_keys('name')
        driver.find_element_by_name('password').send_keys('password')
        # driver.find_element_by_id('dologin').click()

        # tag name 标签名定位
        # driver.find_element_by_tag_name('input').send_keys('Mayvay')

        # class name定位
        # driver.find_element_by_class_name()

        # css定位
        # http://www.w3.org/TR/css3-selectors/
        # http://www.w3school.com.cn/css/css_positioning.asp
        # css_element = driver.find_element_by_css_selector("p.headerTitle")
        # self.assertEqual(css_element.text,"中文邮箱第一品牌")

        # xpanth
        # 什么是 XPath：http://www.w3.org/TR/xpath/
        # XPath 基础教程：http://www.w3schools.com/xpath/default.asp
        # selenium 中被误解的 XPath ： http://magustest.com/blog/category/webdriver/
        # driver.find_element_by_xpath("//*[@name='email']").send_keys("Mayvay")



    def test_print_title(self):
        driver = self.driver
        # 打印title
        print(driver.title)
        # unittest.TestCase提供的断言方法
        self.assertEqual(driver.title, "163网易免费邮--中文邮箱第一品牌")

        # 判断网页打开的title是不是期望的。以下打印出 selenium.webdriver.support.expected_conditions.title_contains object at 0x000002D0158382E0
        ## 有点疑问，打开的网页不存在，也打印出地址了????
        # print(EC.title_contains("免费邮"))

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        cls.driver.quit()


if __name__ == "__main__":
    '''verbosity是一个选项,表示测试结果的信息复杂度，有0、1、2 三个值
    0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共10个 失败2 成功8
    1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”
    2 (详细模式):测试结果会显示每个测试用例的所有相关的信息
    并且 你在命令行里加入不同的参数可以起到一样的效果
    加入 --quiet 参数 等效于 verbosity=0
    加入--verbose参数等效于 verbosity=2
    什么都不加就是 verbosity=1
    '''
    unittest.main(verbosity=2)
