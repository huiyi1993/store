from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get(r"E:/1234/study/automaticday01/练习的html/练习的html/main.html")
driver.switch_to.frame("frame")
driver.find_element_by_xpath("//*[@id='input1']").send_keys("456123")
time.sleep(3)
driver.quit()







