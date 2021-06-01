from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.jd.com/?cu=true&utm_source=haosou-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_haosoupinzhuan&utm_term=0a875d61c5fe47d8bc48679132932d23_0_4bf1ad6708554bea84213b55937d7688")
driver.find_element_by_xpath("//*[@id='ttbar-login']/a[1]").click()
time.sleep(15)
driver.find_element_by_xpath("//*[@id='key']").send_keys("蓝牙耳机")
driver.find_element_by_xpath("//*[@id='search']/div/div[2]/button/i").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[28]/div/div[1]/a/img").click()
time.sleep(5)
wins = driver.window_handles
driver.switch_to.window(wins[1])
driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()
time.sleep(3)
driver.quit()

















