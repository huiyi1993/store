from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome()
driver.get("https://www.qcc.com/?utm_source=baidu1&utm_medium=cpc&utm_term=pzsy")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='addfavorModal']/div/div/div[1]").click()
driver.find_element_by_xpath("/html/body/header/div/ul/li[10]/a/span").click()
time.sleep(2)
ele = driver.find_element_by_xpath("//*[@id='nc_1_n1z']")
ac = ActionChains(driver)
ac.click_and_hold(ele).move_by_offset(348,0).perform()
time.sleep(2)
driver.quit()

















