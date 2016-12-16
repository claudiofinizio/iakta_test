import urllib.request as ur
import json
import codecs

response = ur.urlopen('http://www.iakta.it:3000/travelog/1')
#text = json.loads(response.read())

reader = codecs.getreader("utf-8")
text = json.load(reader(response))



print(text)
