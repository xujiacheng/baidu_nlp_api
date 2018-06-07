# -*- coding: UTF-8 -*-
import json
import sys

def run():
	try: 
		from aip import AipNlp
		
	except: 
		print "Cannot find AipNlp Module. Make sure you import this library. Please check Readme.md for instruction"





def create_client_instance():
	# create a new client
	# return Value: client instance
	APP_ID = '11360135'
	API_KEY = 'XIn7E8ul3puXzC1GeVRSfcv4'
	SECRET_KEY = '8aII6kdOWlU0OKS94f5g3uP9Gf1RPRBq'
	client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
	return client


def get_word_similarity_score(word1, word2):	
	if (word1 is None or word2 is None):
		print "You didn't give correct input format"
		return -1.0

	try:
		client = create_client_instance()
		result = client.wordSimEmbedding(word1, word2)
		score = result.get("score")
		return score
	except:
		print "Something is wrong when calling API method. Please check you have valid APP_ID, API_KEY OR SECRET_KEY"
		return -1.0


def get_shortSentence_similarity_score(sentence1, sentence2):
	if (sentence1 is None or sentence2 is None):
		print "You didn't give correct input format"
		return -1.0

	try:
		client = create_client_instance()
		result = client.simnet(sentence1, sentence2)
		score = result.get("score")
		return score
	except:
		print "Something is wrong when calling API method. Please check you have valid APP_ID, API_KEY OR SECRET_KEY"
		return -1.0


	
