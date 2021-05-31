from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get(r"E:/1234/study/automaticday01/练习的html/练习的html/frame.html")
driver.find_element_by_xpath("//*[@id='input1']").send_keys("123456")
time.sleep(2)
driver.quit()










