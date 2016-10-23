# -*- coding: utf-8 -*-

import time,sys
from subprocess import call
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException


reload(sys)  
sys.setdefaultencoding('utf8')

def translate_text_to_text(translate_str):
	return setup(translate_str)

def speak_translated_text(translate_str):
	translated_str = setup(translate_str)
	call(["say", translated_str])
	return translated_str

def setup(translate_str):
	driver = webdriver.Chrome('/Users/vivekjuneja/Downloads/chromedriver')  
	driver.get('http://labspace.naver.com/nmt/');
	time.sleep(1) 
	encoded_translate_str = unicode(translate_str)
	driver.find_elements(By.XPATH, '//textarea')[0].send_keys(encoded_translate_str)
	driver.find_elements(By.XPATH, '//button')[1].click()

	try:
	    element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//textarea[class()="ta ng-untouched ng-pristine ng-valid" and text() != ""]'))
	)

	except TimeoutException: 
		pass
	finally:
	    text = driver.find_elements(By.XPATH, '//textarea')[1]
	    sys.exc_clear()
	    translated_str = text.get_attribute("value")
	    driver.quit()
	    return translated_str


if __name__ == '__main__':
	speak_translated_text("Hello")
