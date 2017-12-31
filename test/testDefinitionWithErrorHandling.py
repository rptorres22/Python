import re
import urllib.request


try:
    url = "http://dictionary.reference.com/browse/"

    word = input("Enter your word: ")

    url = url + word

    data = urllib.request.urlopen(url).read()
    data1 = data.decode("utf-8")

    #print(data1)

    m = re.search('meta name="description" content="', data1)

    start = m.end()
    end = start + 500

    newString = data1[start:end]

    #print(newString)

    m = re.search(' See more.', newString)
    end = m.start()

    definition = newString[0:end]

    print(definition)

except:
    print("I'm sorry, your word is not in the dictionary.")
