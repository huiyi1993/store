from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome()
driver.get("https://fanyi.baidu.com/#en/zh/element%20click%20intercepted")
driver.find_element_by_xpath("//*[@class='desktop-guide-close']").click()
driver.find_element_by_xpath("//*[@id='main-outer']/div/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/a").click()
ele = driver.find_element_by_xpath("//*[@id='baidu_translate_input']")
ac = ActionChains(driver)
ac.click(ele).key_down("s").key_up("s").key_down("c").key_up("c").perform()















