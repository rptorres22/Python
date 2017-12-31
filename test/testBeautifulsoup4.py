import requests 
from bs4 import *

url = "https://www.accuweather.com/en/us/garden-grove-ca/92843/weather-forecast/332132"
#Needed to add this because of an issue with the server needing the user-agent:
#https://stackoverflow.com/questions/47375153/requests-get-in-python-giving-connection-timeout-error
headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}


data = requests.get(url, headers=headers)
#print(data)


soup = BeautifulSoup(data.text, "html.parser")
data2 = soup.find('div', {'class':'info'})
data3 = data2.find('span', {'class':'large-temp'})
print(data3.contents[0])
