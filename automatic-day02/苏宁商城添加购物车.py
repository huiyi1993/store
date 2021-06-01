from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.suning.com/")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("蓝牙耳机")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()
time.sleep(3)
ele = driver.find_element_by_xpath("//*[@id='ssdsn_search_pro_baoguang-1-0-1_1_05:0000000000_10971678601']/i/img")
ac = ActionChains(driver)
ac.move_to_element(ele).perform()
time.sleep(2)
ac.click(ele).perform()
time.sleep(2)

wins = driver.window_handles
driver.switch_to.window(wins[1])
time.sleep(5)
driver.find_element_by_xpath("//*[@id='addCart']").click()

time.sleep(3)

driver.quit()










