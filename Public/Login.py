import time


class Login(object):
    def __init__(self,driver):
        self.driver=driver

    def login(self):
        time.sleep(5)
        try:
            self.driver.find_element_by_id('cn.xiaochuankeji.tieba:id/close_tv').click()  # 点击同意用户协议
            self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()#同意拨号授权
            time.sleep(2)
            self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()#同意内容访问授权
            time.sleep(2)
            self.driver.find_element_by_id('cn.xiaochuankeji.tieba:id/skip').click()#跳过创建性别
            time.sleep(2)
            self.driver.find_element_by_id('cn.xiaochuankeji.tieba:id/skip').click()#跳过年龄选择
            time.sleep(2)
            self.driver.find_element_by_id('cn.xiaochuankeji.tieba:id/tvConfirmWithBg').click()#同意青少年模式
        except:
            pass
        try:
            self.driver.find_element_by_id('cn.xiaochuankeji.tieba:id/close_tv').click()  # 点击同意用户协议
            self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()  # 同意拨号授权
        except:
            pass
        try:
            self.driver.find_element_by_id('cn.xiaochuankeji.tieba:id/tvConfirmWithBg').click()  # 同意青少年模式
        except:
            pass

        time.sleep(8)
        list_wode=self.driver.find_elements_by_id('cn.xiaochuankeji.tieba:id/textTabItem')
        list_wode[3].click()#进入我的页面
        time.sleep(2)
        try:
            lijidenglu=self.driver.find_elements_by_class_name('//android.widget.TextView[@text="立即登录/注册"]')#定位立即登录/注册
            lijidenglu[4].click()#进入
            time.sleep(2)
            passlogin=self.driver.find_elements_by_class_name('android.widget.TextView')#定位账号密码登录
            passlogin[2].click()#进入
            time.sleep(2)
            phone=self.driver.find_elements_by_class_name('android.widget.EditText')#输入账号
            phone[0].send_keys('15127409611')
            pas=self.driver.find_elements_by_class_name('android.widget.EditText')#输入密码
            pas[1].send_keys('a123456')
            self.driver.find_element_by_class_name('android.widget.Button').click()#点击登录按钮登录
        except:
            pass


        try:
            touxiang=self.driver.find_element_by_id('cn.xiaochuankeji.tieba:id/avatar_view_avatar').is_displayed()
            if touxiang==True:
                zuiyou=self.driver.find_element_by_xpath('//android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView')
                zuiyou.click()
                time.sleep(5)
        except:
            pass













    '''
        for i in range(len(passlogin)):
            print('第' + str(i) + '个=' + passlogin[i].text)
    '''

