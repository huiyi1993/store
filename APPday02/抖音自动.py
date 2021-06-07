from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

import time
server = r"http://localhost:4723/wd/hub"
device_data = {
    "platformName":"Android",
    "deviceName":"127.0.0.1:62001",
    "platformVersion":"7.1.2",
    "appPackage":"com.ss.android.ugc.aweme",
    "appActivity":"com.ss.android.ugc.aweme.splash.SplashActivity"
}
driver = webdriver.Remote(server,device_data)
time.sleep(5)
TouchAction(driver).tap(x=459, y=977).perform()
time.sleep(3)
for i in range(0,10):
    driver.swipe(400,1200,400,200,500)
    time.sleep(20)
driver.quit()













