import os, random, requests


pth = input("Введите папку: ")
try:
	os.mkdir(pth)
	print("*Папка выбрана*")
except OSError:
	print("*Папка выбрана*")

def parse():
	while True:
		url = f"http://static.donationalerts.ru/audiodonations/{random.randint(11111, 99999)}/{random.randint(111,999)}.wav"
		r = requests.get(url)
		if r.status_code == 200:
			with open(pth + '/' + str(random.randint(1,1000000)) + '.wav', 'wb') as f:
				f.write(r.content)
			print(url + " YES")
		else:
			print(url + " NOT")
print('Подождите... Это займёт около минуты!')
parse()
