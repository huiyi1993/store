from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get(r"E:/1234/study/automaticday01/练习的html/练习的html/弹框的验证/dialogs.html")
driver.find_element_by_xpath("//*[@id='alert']").click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(3)
driver.quit()












