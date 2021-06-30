### Windows  Jenkins持续集成项目搭建- 基于Python Selenium自动化测试

**Jenkins环境准备**　　

　　使用了unittest的TestSuite Runner批量执行测试，并以**JUnit**报告的格式输出测试结果。这里需要用到Python下的**xmlrunner**库。执行以下命令下载与安装xmlrunner。

```python
　　pip install xmlrunner
```

　用xmlrunner.XMLTestRunner来运行冒烟测试并生成JUnit测试报告。此报告以XML格式生成，保存在“测试报告”子文件夹中。代码如下：

```python
import unittest
from xmlrunner import xmlrunner
from studytest.start_browser import Login
from studytest.HomePage import HomePageTest

# 取到所有的测试用例
# TestLoader类，可以得到指定的测试文件中的测试方法且用于测试套件
login_tests = unittest.TestLoader().loadTestsFromTestCase(Login)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# 创建一个测试套件（TestSuite）
smoke_tests = unittest.TestSuite([home_page_tests, login_tests])

# 执行测试套件用XMLrunner
# 生成的报告在当前项目路径下“测试报告”文件夹内
xmlrunner.XMLTestRunner(verbosity=2, output='测试报告').run(smoke_tests)
```

**搭建Jenkins**

下载：[Jenkins官网](https://www.jenkins.io/download/)

1. 点击jenkins.msi进行安装，一路next就行，对于安装路径可以自定义点击change进行更换自己的空间就行，然后Install

2. 当安装完以后点击Finish 会出现,点击Finish浏览器会自动打开 [http://localhost:8080/](https://links.jianshu.com/go?to=http%3A%2F%2Flocalhost%3A8080%2F)，等待加载后，如下图

   ![](https://cdn.jsdelivr.net/gh/ChenZhiM/cloudimg@main/data/20210622232245.png)

3. 根据密码路径，将initialAdminPassword文件中生成的密码复制到文本框中点击继续。注：此处遇到问题1：我的电脑中展示的路径文件夹为0字节，打不开。我自己的处理方式通过cmd命令行打开文件（type 密码文件路径），暂未了解的原因，希望知道的能告诉我原因。

4. 进入安装界面，我选择的是推荐性安装，因为不知道每个插件都是什么作用，点击安装之后出现这个页面，进行等待

5. 用户密码的设置，进行信息的完善之后选择保存，这样就可以进入jenkins的首页，当以后再次登陆的时候就会进行登陆页面，使用用户名密码进行登录

   ![](https://cdn.jsdelivr.net/gh/ChenZhiM/cloudimg@main/data/20210622232324.png)

6. 在Jenkins Dashboard页面上，单击**新建项目**（New Item）链接，创建一个新的Jenkins作业，如下图所示

   ![](https://cdn.jsdelivr.net/gh/ChenZhiM/cloudimg@main/data/20210622232101.png)

7. 在项目名称（Item name）文本框中输入 job名称（如Demo_Smoke_Test），然后选择**构建自由风格的软件项目**（Freestyle project）单选按钮，单击**确定**（OK）按钮。以上指定名称命名的新作业就创建成功了。如下图所示：![](https://cdn.jsdelivr.net/gh/ChenZhiM/cloudimg@main/data/20210622232515.png)

8. 在构建（Bulid）部分，单击**增加构建步骤**（Add build step），然后从下拉列表中选择执行Windows批处理命令（Execute Windows batch command）选项，如下图所示；在**命令（Command）**文本框里输入以下命令，如下图所示。这个命令将冒烟测试的Python脚本文件复制到Jenkins工作空间下并执行smoketest.py。

   ![](https://cdn.jsdelivr.net/gh/ChenZhiM/cloudimg@main/data/20210622233606.png)

9. 在前面已经配置了smoketest.py以生成JUnit格式的测试结果，并将测试结果显示在Jenkins Dashboard页面。要在Jenkins中集成这些报告，先单击**增加构建后操作步骤**（Add post-build action），然后选择发布JUnit测试结果报告（**Publish JUnit test result report**）选项，如下图所示；在构建后操作（Post-build Aactions）部分中，在**测试报告XML**（Test report XMLs）文本框中添加“测试报告/*.xml”，如下图所示。Jenkins每次运行测试的时候，它将从“测试报告”子文件夹中读取测试结果。

   ![](https://cdn.jsdelivr.net/gh/ChenZhiM/cloudimg@main/data/20210622233958.png)

10. 由于需要按计划时间自动执行测试，在**构建触发器**（Build Triggers）部分选择**定期构建**（Build periodically），并在**计划**（Schedule）文本框中输入如下图所示数据。那么，每天下午18:24构建过程将自动触发，作为无人值守构建过程的一部分，Jenkins也将自动执行测试，这样在第二天早上当你到达办公室的时候就可以看到测试执行结果了。

    ![](https://cdn.jsdelivr.net/gh/ChenZhiM/cloudimg@main/data/20210622234236.png)

11. 如果想只保留最近构建记录和次数，勾选**Discard old builds**,根据自己情况设置内容后点击“保存”按钮![](https://cdn.jsdelivr.net/gh/ChenZhiM/cloudimg@main/data/20210622233218.png)

12. 现在可以来检测一下所有的配置是否设置好，测试是否能成功执行。单击**立即构建**（Build Now）链接手动运行该作业，如下图所示：

    ![](https://cdn.jsdelivr.net/gh/ChenZhiM/cloudimg@main/data/20210622234508.png)

13. 单击**构建历史**（Build History）部分中正在运行的项目。除了Jenkins页面上的执行状态和进度条，还可以通过打开**控制台输出**（Console Output）链接观察后执行信息，可查看报错信息。

14. **注：**构建时失败遇到的问题：

    **问题一**：python不是内部或外部命令

    原因：把Jenkins项目配置中 python xxx.py  修改成python可执行文件全路径：D:\Python35\python.exe xxx.py ，再次构建也没有问题。这是因为 Jenkins 缺少环境配置。

    解决方案：配置构建执行状态：

    1.回到 Jenkins 首页，点击 “构建执行状态”（Build Executor Status） ,右则会列出本机信息。

    2.点击本机设置按钮，配置 Python 的 path 环境变量。同时还需要添加浏览器驱动文件所在目录

    ![](https://cdn.jsdelivr.net/gh/ChenZhiM/cloudimg@main/data/20210622235322.png)

    ![](https://cdn.jsdelivr.net/gh/ChenZhiM/cloudimg@main/data/20210622235503.png)

    **问题二：**报ImportError: No module named xmlrunner的问题

    原因：暂不了解原因，解决方案参考[解决jenkins或cmd中运行python脚本报ImportError: No module named xmlrunner的问题](https://blog.csdn.net/weixin_40188140/article/details/86713925)

    现直接在脚本**最上方**添加两行代码，将打印出的路径均添加语句sys.path.append("")，有多少个路径添加多少条append，如sys.path.append("E:\\PycharmProjects\\autoInterface\\wjhtest")这种写法

    ```python
    import sys
    print (sys.path)
    sys.path.append("E:\\PycharmProjects\\autoInterface\\wjhtest")
    ```

    **问题三：** 报错：UnicodeEncodeError: 'gbk' codec can't encode character '\xa9' in position 449: illegal multibyte sequence

    参考：[jenkins运行脚本 报错：UnicodeEncodeError: 'gbk' ](https://www.cnblogs.com/liulinghua90/p/13255960.html)

    解决方案：在自己的脚本里面添加这两句代码

    ```python
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb18030")
    ```

15. 以上构建成功后，Jenkins通过读取unittest框架生成的测试文件，在页面上显示测试结果和其他各项指标。单击构建页面上的**测试结果**（Test Results）链接可以查看Jenkins保存的测试结果。之前配置的测试结果以JUnit格式生成。当单击测试结果（Test Results）时，Jenkins将会**显示JUnit测试结果**，如下图所示，显示测试结果摘要，其中失败的测试会高亮显示。

    我们也可以单击**Package**名字的链接来查看各个测试的详细结果信息![](https://cdn.jsdelivr.net/gh/ChenZhiM/cloudimg@main/data/20210623000627.png)

    　　综上所述，**通过搭建Jenkins运行Python Selenium测试，从而实现每天晚上在无人值守的情况下自动构建程序和执行测试。即实现了简单的持续集成测试。**

    

