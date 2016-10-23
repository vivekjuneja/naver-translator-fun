# -*- coding: utf-8 -*-

import time,sys,os
from subprocess import call
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException


reload(sys)  
sys.setdefaultencoding('utf8')
webdriver_type=os.environ['WEBDRIVER']


sentence_split_threshold=200

def split(translate_text):
	translate_text_array = unicode(translate_text).split(" ")
	translated_sentences_buffer = []
	each_sentence = ""
	char_counter=0
	sentence_counter = 0;
	print len(translate_text_array)
	for each_word in translate_text_array:
		word_length = len(each_word)
		print str(char_counter + word_length) + " " + each_word
		if((char_counter + word_length) < sentence_split_threshold):
			char_counter += (word_length+1)
			each_sentence+=(each_word + " ")
		else:
			print each_sentence
			char_counter = 0;
			translated_sentences_buffer.append(each_sentence)
			#print each_sentence
			each_sentence=""


	translated_sentences_buffer.append(each_sentence)

	print (len(translated_sentences_buffer))
	
	return translated_sentences_buffer


def translate_text_to_text(translate_str):
	return setup(translate_str)

def speak_translated_text(translate_str):
	translated_str = setup(translate_str)
	call(["say", translated_str])
	return translated_str

def setup(translate_str):
	translated_sentences_buffer = split(translate_str)
	if webdriver_type=="chrome":
		driver = webdriver.Chrome() 
	elif webdriver_type=="phantomjs":
		driver = webdriver.PhantomJS()	

	print len(translated_sentences_buffer)
	translated = ""
	for each_sentence_to_translate in translated_sentences_buffer:
		driver.get('http://labspace.naver.com/nmt/');
		#time.sleep(1) # Let the user actually see something!
		encoded_translate_str = (each_sentence_to_translate)
		print "To Translate : " + encoded_translate_str
		driver.find_elements(By.XPATH, '//textarea')[0].send_keys(encoded_translate_str)
		driver.find_elements(By.XPATH, '//button')[1].click()

		try:
		    element = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, '//textarea[class()="ta ng-untouched ng-pristine ng-valid" and text() != ""]'))
		)

		except TimeoutException: 
			pass
		finally:
		    text = driver.find_elements(By.XPATH, '//textarea')[1]
		    sys.exc_clear()
		    translated_str = text.get_attribute("value")
		    translated = translated + translated_str


	driver.quit()
	print (translated)
	return translated


if __name__ == '__main__':
	print setup("강호인 국토교통부 장관은 지난 14일 국회 국토교통위원회 국정감사에서")
	speak_translated_text("Hello")
