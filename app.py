#!flask/bin/python
# -*- coding: UTF-8 -*
import json
import sys
from flask import Flask, jsonify
try: 
	from aip import AipNlp
except: 
	print "Cannot find AipNlp Module. Make sure you have this library. Please check README.md for instruction"

app = Flask(__name__)

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
#query_result = [{'id':1, 'score' : 0.45, 'done':True, 'word1': "深圳",' word2': "北京" }]

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/nlp/api/v1.0/query_result/<string:words>', methods = ['GET'])
def get_query_result(words):
	try:
		success = False
		mylist = words.split(',')
		word1 = mylist[0]
		word2 = mylist[1]
		score = get_word_similarity_score(word1,word2)
		if (score > 0):
			success = True
		current_result = [{'similarity_score': score, 'word1': word1, 'word2':word2, 'success':success }]
		return jsonify({'query_result':current_result})
	except: 
		abort(404)


if __name__ == '__main__':
    app.run(debug=True)









