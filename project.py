import random
import requests
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
			req = requests.get(url, stream=True)
			if __name__ == '__main__':
				if req.status_code == 200:
					with open(str(random.randint(1,1000000)) + '.wav', 'wb') as f:
						f.write(req.content)
			print(url)
parse()
