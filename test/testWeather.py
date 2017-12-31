import re
import urllib.request

#https://www.weather-forecast.com/locations/Dublin/forecasts/latest

city = input("Enter your city: ")
url = "https://www.weather-forecast.com/locations/" + city + "/forecasts/latest"

data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")

#print(data1)

m = re.search('<span class="phrase">', data1)

start = m.end()
end = start + 500

newString = data1[start:end]

#print(newString)

m = re.search('</span>', newString)

end = m.start()

final = newString[0:end]

print(final)