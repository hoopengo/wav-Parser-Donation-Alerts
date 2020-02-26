import random
import requests
import os

i = 0

def parse():
	while True:
		url = "http://static.donationalerts.ru/audiodonations/"
		a = random.randint(11111, 99999)
		b = random.randint(111,999)
		url = url + str(a) + '/'
		url = url + str(a) + str(b) + ".wav"
		session = requests.Session()
		request = session.get(url)
		if request.status_code != 404:
			print(url)
parse()
