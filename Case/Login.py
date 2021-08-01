from appium import webdriver
import unittest
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'#定义系统
        desired_caps['platformVersion']='7.1.2'#定义系统版本
        desired_caps['deviceName']='OPPO'#定义设备名称
        #desired_caps['noReset']='True'#调试模式，设置为不初始化
        desired_caps['fullReset'] = 'True'  # 每条用例跑完重置app
        desired_caps['app']=('H:/软件测试/Zuiyouapp/zuiyou.latest.pc-guanwang.apk')
        desired_caps['appPackage']='cn.xiaochuankeji.tieba'#获取app包名
        desired_caps['appActivity']='.ui.base.SplashActivity'#获取app activity路径

        self.abc=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)#建立远程连接，把desired_caps数据传输到appium server端
        time.sleep(5)

    def tearDown(self):
        filedir = "H:/软件测试/Zuiyouapp/test/screenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('//', 'test', 'screenshot'))
        print("endTime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.abc.get_screenshot_as_file(screen_name)
        self.abc.quit()

    def testZy_001(self):
        '''登录-同意用户协议'''
        title=self.abc.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.TextView[1]').text#拿到标题文本
        agreement = self.abc.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.TextView[2]').text#拿到协议文本
        time.sleep(2)
        self.abc.find_element_by_id('cn.xiaochuankeji.tieba:id/close_tv').click()  # 点击同意用户协议

        self.abc.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()  # 同意拨号授权
        time.sleep(2)
        self.abc.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()  # 同意内容访问授权
        time.sleep(5)
        title_sex=self.abc.find_elements_by_class_name('android.widget.TextView')
        #title_sex=WebDriverWait(self.abc,10,0.1).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'android.widget.TextView')))
        for i in range(len(title_sex)):
            print('str[i]  '+title_sex[i].text)
        #title_sex=title_sex.text
        #title_sex=self.abc.find_element_by_id('cn.xiaochuankeji.tieba:id/main_title').text#拿到性别选择页title

        self.assertEqual('用户协议及隐私政策',title)
        self.assertEqual("本《用户协议》及《隐私政策》将向你说明：\n1、为帮助你浏览推荐、发布内容、交流沟通、注册账号，我们可能会收集联络方式、位置、音视频等敏感信息，你有权拒绝或撤回授权\n2、未经你同意，我们不会从第三方获取、共享或对外提供你的信息\n3、你可以访问、更正、删除你的个人信息，我们也提供注销、投诉方式\n详情请查看《用户协议》《隐私政策》",agreement)
        #self.assertEqual('-选择你的性别-',title_sex)

    def testZy_002(self):
        '''登录-检查选择性别页面’'''
        self.abc.find_element_by_id('cn.xiaochuankeji.tieba:id/close_tv').click()  # 点击同意用户协议
        try:
            self.abc.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()  # 同意拨号授权
            time.sleep(2)
            self.abc.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()  # 同意内容访问授权
            time.sleep(2)
        except:
            pass
        time.sleep(5)
        pass_text = self.abc.find_element_by_xpath('//android.widget.RelativeLayout/android.widget.TextView[1]').text  # 拿到跳过按钮文本
        title_sex = self.abc.find_element_by_xpath('//android.widget.RelativeLayout/android.widget.TextView[2]').text  # 拿到性别选择页title
        choose_sex=self.abc.find_element_by_xpath('//android.widget.RelativeLayout/android.widget.TextView[3]').text   # 拿到性别选择提醒
        boy_text=self.abc.find_element_by_xpath('//*[@resource-id="cn.xiaochuankeji.tieba:id/ivMale_title"]').text#拿到我是男生文本
        girl_text = self.abc.find_element_by_xpath('//*[@resource-id="cn.xiaochuankeji.tieba:id/ivFemale_title"]').text  # 拿到我是女生文本

        self.assertEqual('跳过  ',pass_text)
        self.assertEqual('让最右更懂你',title_sex)
        self.assertEqual('-选择你的性别-',choose_sex)
        self.assertEqual('我是男生',boy_text)
        self.assertEqual('我是女生',girl_text)

    def testZy_003(self):
        '''登录-选择性别-选择我是男生'''
        self.abc.find_element_by_id('cn.xiaochuankeji.tieba:id/close_tv').click()  # 点击同意用户协议
        try:
            self.abc.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()  # 同意拨号授权
            time.sleep(2)
            self.abc.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()  # 同意内容访问授权
            time.sleep(2)
        except:
            pass
        time.sleep(5)
        self.abc.find_element_by_xpath('//android.widget.TextView[@text="我是男生"]/../android.widget.ImageView').click()#点击我是男生
        time.sleep(3)
        chose_age=self.abc.find_element_by_xpath('//android.widget.TextView[3]').text

        self.assertEqual('-选择年龄，推荐更精准-',chose_age)

    def testZy_004(self):
        '''登录-选择性别-选择我是女生'''
        self.abc.find_element_by_id('cn.xiaochuankeji.tieba:id/close_tv').click()  # 点击同意用户协议
        try:
            self.abc.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()  # 同意拨号授权
            time.sleep(2)
            self.abc.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()  # 同意内容访问授权
            time.sleep(2)
        except:
            pass
        time.sleep(5)
        self.abc.find_element_by_xpath(
            '//android.widget.TextView[@text="我是女生"]/../android.widget.ImageView').click()  # 点击我是女生
        time.sleep(3)
        chose_age = self.abc.find_element_by_xpath('//android.widget.TextView[3]').text

        self.assertEqual('-选择年龄，推荐更精准-', chose_age)

    def testZy_005(self):
        '''登录-选择性别-选择跳过'''
        self.abc.find_element_by_id('cn.xiaochuankeji.tieba:id/close_tv').click()  # 点击同意用户协议
        try:
            self.abc.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()  # 同意拨号授权
            time.sleep(2)
            self.abc.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()  # 同意内容访问授权
            time.sleep(2)
        except:
            pass
        time.sleep(5)
        self.abc.find_element_by_xpath('//*[@text="跳过  "]').click()  # 点击我跳过
        time.sleep(3)
        chose_age = self.abc.find_element_by_xpath('//android.widget.TextView[3]').text

        self.assertEqual('-选择年龄，推荐更精准-', chose_age)

    def testZy_006(self):
        '''登录-检查选择年龄页面'''
        self.abc.find_element_by_id('cn.xiaochuankeji.tieba:id/close_tv').click()  # 点击同意用户协议
        try:
            self.abc.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()  # 同意拨号授权
            time.sleep(2)
            self.abc.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()  # 同意内容访问授权
            time.sleep(2)
        except:
            pass
        time.sleep(5)
        self.abc.find_element_by_xpath('//*[@text="跳过  "]').click()  # 点击我跳过
        time.sleep(3)
        title=self.abc.find_element_by_xpath('//android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.TextView[2]').text#获取标题
        title_2 = self.abc.find_element_by_xpath(
            '//android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.TextView[3]').text#获取二层标题
        age16=self.abc.find_element_by_xpath('//android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.TextView').text#获得第一个选项文本
        age16_18 = self.abc.find_element_by_xpath(
            '//android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]/android.widget.TextView').text#获得第二个选项文本
        age19_22 = self.abc.find_element_by_xpath(
            '//android.widget.RelativeLayout/android.widget.LinearLayout[3]/android.widget.RelativeLayout[2]/android.widget.TextView').text#获得第三个选项文本
        age22 = self.abc.find_element_by_xpath(
            '//android.widget.RelativeLayout/android.widget.LinearLayout[4]/android.widget.RelativeLayout[2]/android.widget.TextView').text#获得第四个选项文本

        self.assertEqual('让最右更懂你',title)
        self.assertEqual('-选择年龄，推荐更精准-',title_2)
        self.assertEqual('不满16岁',age16)
        self.assertEqual('16-18岁',age16_18)
        self.assertEqual('19-22岁',age19_22)
        self.assertEqual('22岁以上',age22)























