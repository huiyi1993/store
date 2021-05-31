from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get(r"E:/1234/study/automaticday01/练习的html/练习的html/上传文件和下拉列表/autotest.html")
driver.find_element_by_xpath("//*[@name='account']").send_keys("huiyi")
driver.find_element_by_xpath("//*[@name='password']").send_keys("huiyi")
driver.find_element_by_xpath("//*[@id='areaID']").send_keys("北京")
driver.find_element_by_xpath("//*[@id='sexID1']").click()
driver.find_element_by_xpath("//*[@value='spring']").click()
driver.find_element_by_xpath("//input[@name='file']").send_keys(r"E:\1234\study\automaticday01\景甜.jpg")
driver.find_element_by_xpath("//*[@id='buttonID']").click()
time.sleep(2)
driver.quit()















