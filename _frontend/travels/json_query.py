import urllib.request as ur
import json
import codecs
        
        
def decode_from_iakta_website(requested_url):
    response = ur.urlopen(requested_url)
    reader = codecs.getreader("utf-8")
    return json.load(reader(response))
