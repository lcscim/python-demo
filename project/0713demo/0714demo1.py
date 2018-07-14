from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_xpath("//*[@text='1']").click()

driver.find_element_by_xpath("//*[@text='5']").click()

driver.find_element_by_xpath("//*[@text='9']").click()

# driver.find_element_by_xpath("//*[@text='DEL']").click()

driver.find_element_by_xpath("//*[@text='9']").click()

driver.find_element_by_xpath("//*[@text='5']").click()

driver.find_element_by_xpath("//*[@text='+']").click()

driver.find_element_by_xpath("//*[@text='6']").click()

driver.find_element_by_xpath("//*[@text='=']").click()
time.sleep(5)

driver.quit()
