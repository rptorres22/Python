import re
import urllib.request

url = "https://finance.google.com/finance?q="

#stock = input("Enter your stock: ")

stocks = ["FB", "GOOGL", "MSFT", "INTC"]

for i in range(len(stocks)):
    searchurl = url + stocks[i]

    data = urllib.request.urlopen(searchurl).read()

    data1 = data.decode("utf-8")

    m = re.search('meta itemprop="price"', data1)

    start = m.start()
    end = start + 50
    newString = data1[start:end]

    m = re.search('content="', newString)
    start = m.end()
    newString1 = newString[start:]

    m = re.search("/", newString1)
    end = m.end()-3
    final = newString1[0:end]
    print("The value of " + stocks[i].upper() + " is " + final)

