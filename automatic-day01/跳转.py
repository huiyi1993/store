from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get(r"E:/1234/study/automaticday01/练习的html/练习的html/跳转页面/pop.html")
driver.find_element_by_xpath("//*[@id='goo']").click()
time.sleep(3)
driver.quit()
