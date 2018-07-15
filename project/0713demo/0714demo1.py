from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Android Emulator'

desired_caps['app'] = r'com.google.android.calculator.apk'


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

