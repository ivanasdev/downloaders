#Downloads google image

import requests
url = input("URL: ")

r = requests.get(url)

#Create path for image
path = input('Nombrar archivo: ')

with open(path, "wb") as f:
	f.write(r.content)
