# -*- coding: utf-8 -*-

import time,sys,os,json
from subprocess import call
import httplib, urllib


reload(sys)  
sys.setdefaultencoding('utf8')

target="ko"
source="en"

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
	translated_text = ""
	print "Hello"
	global target
	global source
	print ord(translate_str[1:2])
	if(ord(translate_str[1:2])>122):
		 target="en"
		 source="ko"
	elif(ord(translate_str[1:2])<=122):
		target="ko"
		source="en"

	print source, target
	for to_translate in split(translate_str):
		translated_text+=call_translator(to_translate)

	return translated_text

def speak_translated_text(translate_str):
	translated_str = translate_text_to_text(translate_str)
	call(["say", translated_str])
	return translated_str

def call_translator(translate_str):
	NAVER_MNT_HOST = 'labspace.naver.com'
	NAVER_MNT_PORT = 80

	conn = httplib.HTTPConnection(NAVER_MNT_HOST, NAVER_MNT_PORT)
	conn.set_debuglevel(1)
	conn.connect()

	print source, target
	params = urllib.urlencode({
	    'source': source,
	    'target': target,
	    'text': translate_str
	})


	headers = {
	    "content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
	}

	request = conn.request('POST', '/api/n2mt/translate', params, headers)

	response = conn.getresponse()
	response_json = json.loads(response.read())

	print response.status
	print response.reason
	translated = response_json["message"]["result"]["translatedText"]
	return translated

	conn.close()


if __name__ == '__main__':
	print translate_text_to_text("교통부 장관")
	
	#speak_translated_text("Hello")
