# -*- coding: UTF-8 -*-
import json
import sys


from aip import AipNlp


def run():
	



def get_similarity_score(word1, word2)
	
	if (word1 is None or word2 is None):
		print "" 
	APP_ID = '11360135'
	API_KEY = 'XIn7E8ul3puXzC1GeVRSfcv4'
	SECRET_KEY = '8aII6kdOWlU0OKS94f5g3uP9Gf1RPRBq'

	client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
	#word1 = "北京"
	#word2 = "上海"

	""" 调用词义相似度 """
	client.wordSimEmbedding(word1, word2);

	""" 如果有可选参数 """
	options = {}

	""" 带参数调用词义相似度 """
	result = client.wordSimEmbedding(word1, word2, options)
	score = result.get("score")
	print score
