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
	driver = webdriver.Chrome('/Users/vivekjuneja/Downloads/chromedriver')  # Optional argument, if not specified will search path.
	
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
		    element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//textarea[class()="ta ng-untouched ng-pristine ng-valid" and text() != ""]'))
		)

		except TimeoutException: 
			pass
		finally:
		    text = driver.find_elements(By.XPATH, '//textarea')[1]
		    sys.exc_clear()
		    translated_str = text.get_attribute("value")
		    translated = translated + translated_str



	driver.quit()
	return translated

if __name__ == '__main__':
	print setup("재판부는 귀가해 예상치 못한 상황을 목격한 피고인은 A씨가 해명도 없이 옷을 챙겨입고 급히 자리를 떠나려 하자 그 상황에 대한 증거를 확보하기 위해 촬영한 것으로 보인다며 경찰이 출동할 때까지 기다려 증거를 확보하는 등 다른 법적 조치를 찾아볼 만한 시간적 여유가 없었던 것으로 판단돼 피고인의 이 부분에 대한. 재판부는 귀가해 예상치 못한 상황을 목격한 피고인은 A씨가 해명도 없이 옷을 챙겨입고 급히 자리를 떠나려 하자 그 상황에 대한 증거를 확보하기 위해 촬영한 것으로 보인다며 경찰이 출동할 때까지 기다려 증거를 확보하는 등 다른 법적 조치를 찾아볼 만한 시간적 여유가 없었던 것으로 판단돼 피고인의 이 부분에 대한")
	#speak_translated_text("Hello")
