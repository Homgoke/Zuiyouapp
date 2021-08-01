import time
import unittest


class Tuijian(object and unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver

    def inTuijian(self):
        tuijian = self.driver.current_activity  # 判断进入推荐页面
        self.assertIn('.ui.home.page.PageMainActivity',tuijian)
        time.sleep(3)