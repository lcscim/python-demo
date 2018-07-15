from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'samsung-sm_a9100-2369b073'
desired_caps['appPackage'] = 'com.example.rongyuntest'
desired_caps['appActivity'] = '.start.MainActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'华为')]").click()
driver.find_element_by_id("com.example.rongyuntest:id/phone_name").click()

time.sleep(5)

driver.quit()
