from appium import webdriver
import unittest
import os
import time
from Public.Tuijian import Tuijian
from Public.Refresh import Refresh
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Public.Login import Login


class Zhuye(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'#定义系统
        desired_caps['platformVersion']='7.1.2'#定义系统版本
        desired_caps['deviceName']='NOX'#定义设备名称
        #desired_caps['noReset']='True'#调试模式，设置为不初始化
        desired_caps['fullReset'] = 'True'  # 每条用例跑完重置app
        desired_caps['app']=('H:/软件测试/Zuiyouapp/zuiyou.latest.pc-guanwang.apk')
        desired_caps['appPackage']='cn.xiaochuankeji.tieba'#获取app包名
        desired_caps['appActivity']='.ui.base.SplashActivity'#获取app activity路径
        #desired_caps['automationName']='Uiautomator2'#定义toast控件
        #desired_caps['unicodeKeyboard']='Ture'#安装输入法
        #desired_caps['resetKeyboard']='Ture'#初始化输入法



        self.abc=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)#建立远程连接，把desired_caps数据传输到appium server端
        time.sleep(2)

    def tearDown(self):
        filedir = "H:/软件测试/Zuiyouapp/test/screenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('//', 'test', 'screenshot'))
        print("endTime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.abc.get_screenshot_as_file(screen_name)
        self.abc.quit()

    def testZy_007(self):
        '''推荐-刷新成功'''
        Login(self.abc).login()
        tuijian=self.abc.current_activity#判断进入推荐页面
        windowsize=self.abc.get_window_size()
        conten1=self.abc.find_element_by_xpath('//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.TextView').text#刷新前第一条内容
        time.sleep(2)
        height=windowsize['height']
        width=windowsize['width']
        self.abc.swipe(width*0.5,height*0.3,width*0.5,height*0.8,3000)#下拉刷新
        new_text=self.abc.find_element_by_id('cn.xiaochuankeji.tieba:id/content_label').text
        time.sleep(2)
        conten2=self.abc.find_element_by_xpath('//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.TextView').text#刷新后第一条内容

        self.assertEqual('.ui.home.page.PageMainActivity',tuijian)
        self.assertIn('为你选出',new_text)
        self.assertTrue(conten1!=conten2)
        # if conten1!=conten2:
        #     pass
        # else:
        #     self.assertEqual('False',conten1)

    def testZy_008(self):
        '''推荐-评论成功'''
        Login(self.abc).login()
        tuijian = self.abc.current_activity  # 判断进入推荐页面
        self.assertEqual('.ui.home.page.PageMainActivity', tuijian)
        self.abc.find_element_by_id('cn.xiaochuankeji.tieba:id/middle_view').click()#点击评论按钮
        time.sleep(2)
        self.abc.find_element_by_id('cn.xiaochuankeji.tieba:id/etInput').click()
        time.sleep(2)
        self.abc.find_element_by_id('cn.xiaochuankeji.tieba:id/etInput').send_keys('哈1哈哈哈哈哈1')#输入评论
        self.abc.implicitly_wait(3)
        self.abc.find_element_by_xpath('//android.widget.TextView[@text="发送"]').click()#点击发送
        send_ok=WebDriverWait(self.abc,10,0.1).until(EC.presence_of_element_located((By.XPATH,'//*[contains(@text,"评论发送成功")]'))).text
        time.sleep(3)
        first_send=self.abc.find_element_by_xpath('//android.widget.LinearLayout[@resource-id="cn.xiaochuankeji.tieba:id/v_base_comment_content"][1]/android.widget.TextView').text#定位第一条评论内容


        self.assertEqual('评论发送成功',send_ok)
        self.assertEqual('哈1哈哈哈哈哈1',first_send)

    def testZy_009(self):
        '''推荐-收藏成功'''
        Login(self.abc).login()
        Tuijian(self.abc).inTuijian()#进入推荐页
        Refresh(self.abc).Refresh()#刷新页面
        first_id=self.abc.find_elements_by_id('cn.xiaochuankeji.tieba:id/simple_member_tv_name')[0].text
        first_nr=self.abc.find_elements_by_id('cn.xiaochuankeji.tieba:id/expand_content_view')[0].text
        try:#如果出现9图无法定位转发按钮，则刷新
            for i in range(10):
                zfbt = self.abc.find_element_by_id('cn.xiaochuankeji.tieba:id/operate_share').is_displayed()  # 定位转发按钮
                if zfbt==False:
                    Refresh(self.abc).Refresh()
        except:
            pass

        time.sleep(5)
        self.abc.find_element_by_id('cn.xiaochuankeji.tieba:id/operate_share').click()#点击转发按钮
        sc=WebDriverWait(self.abc,10,0.1).until(EC.presence_of_all_elements_located((By.ID,'cn.xiaochuankeji.tieba:id/ivIcon')))#点击收藏按钮
        sc[6].click()
        time.sleep(3)
        scdir=WebDriverWait(self.abc,10,0.1).until(EC.presence_of_all_elements_located((By.ID,'cn.xiaochuankeji.tieba:id/tvName')))#选择第一个收藏夹
        scdir[1].click()
        scsuc=WebDriverWait(self.abc,10,0.1).until(EC.presence_of_element_located((By.XPATH,'//*[contains(@text,"收藏成功")]'))).text
        time.sleep(5)
        wd=WebDriverWait(self.abc,10,0.1).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'android.widget.TextView')))
        #wd=self.abc.find_elements_by_class_name('android.widget.TextView')#点击我的
        wd[4].click()
        # for i in range(len(wd)):
        #     print(str(i)+'==='+str(wd[i].text))
        time.sleep(2)
        self.abc.find_element_by_id('cn.xiaochuankeji.tieba:id/my_favor_icon').click()#点击我的收藏
        time.sleep(2)
        scdir1 = WebDriverWait(self.abc, 10, 0.1).until(
            EC.presence_of_all_elements_located((By.ID, 'cn.xiaochuankeji.tieba:id/my_favor_item_name')))  # 选择第一个收藏夹
        scdir1[0].click()
        time.sleep(5)
        scfirst_id=self.abc.find_elements_by_id('cn.xiaochuankeji.tieba:id/simple_member_tv_name')[0].text#收藏夹第一条id
        scfitst_nr=self.abc.find_elements_by_id('cn.xiaochuankeji.tieba:id/expand_content_view')[0].text#收藏夹第一条内容




        self.assertEqual('收藏成功',scsuc)
        self.assertEqual(first_id,scfirst_id)
        self.assertEqual(first_nr,scfitst_nr)










