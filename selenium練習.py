# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 載入需要的套件
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 開啟瀏覽器視窗(Chrome)
# 方法一：執行前需開啟chromedriver.exe且與執行檔在同一個工作目錄
driver = webdriver.Chrome()
# 方法二：或是直接指定exe檔案路徑 driver = webdriver.Chrome(“桌面\chromedriver”)

# 進入google
driver.get("http://www.google.com") 
# 定位搜尋框
element = driver.find_element(By.CLASS_NAME, "gLFyf")
# 傳入字串
element.send_keys("ntpu")
element.send_keys(Keys.RETURN)

