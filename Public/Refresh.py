import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Refresh(object and unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver

    def Refresh(self):
        windowsize = self.driver.get_window_size()
        height = windowsize['height']
        width = windowsize['width']
        self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8, 3000)  # 下拉刷新
        aler=WebDriverWait(self.driver,10,0.1).until(EC.presence_of_element_located((By.ID,'cn.xiaochuankeji.tieba:id/content_label')))
        new_text=aler.text
        #new_text = self.driver.find_element_by_id('cn.xiaochuankeji.tieba:id/content_label').text
        self.assertIn('为你选出', new_text)
        time.sleep(5)

