import random
import requests
def parse():
	while True:
		url = "http://static.donationalerts.ru/audiodonations/"
		a = random.randint(11111, 99999)
		b = random.randint(111,999)
		url = url + str(a) + '/'
		url = url + str(a) + str(b) + ".wav"
		s = requests.Session()
		r = s.get(url, stream=True)
		if r.status_code == 200:
			with open(str(random.randint(1,1000000)) + '.wav', 'wb') as f:
				f.write(r.content)
			print(url)
parse()