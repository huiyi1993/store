from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

server = r"http://localhost:4723/wd/hub"
desired_capabilities = {
    "platformName":"Android",
    "deviceName":"127.0.0.1:62001",
    "platformVersion":"7.1.2",
    "appPackage":"com.jingdong.app.mall",
    "appActivity":"com.jingdong.app.mall.main.MainActivity"
}
driver = webdriver.Remote(server,desired_capabilities)
time.sleep(3)
TouchAction(driver).tap(x=452, y=1219).perform()
time.sleep(30)
TouchAction(driver).tap(x=392, y=196).perform()
time.sleep(3)
el2 = driver.find_element_by_id("com.jd.lib.search.feature:id/zw")
el2.send_keys("蓝牙耳机")
time.sleep(3)
TouchAction(driver).tap(x=840, y=105).perform()
time.sleep(5)
TouchAction(driver).tap(x=203, y=553).perform()
time.sleep(5)
TouchAction(driver).tap(x=550, y=1548).perform()
time.sleep(5)
TouchAction(driver).tap(x=448, y=1548).perform()
time.sleep(5)
driver.quit()































