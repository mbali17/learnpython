'''
documentation:https://www.crummy.com/software/BeautifulSoup/bs4/doc/
BeustifulSoup is library used to parse html and xml.
'''
from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('http://feeds.reuters.com/news/artsculture?format=xml')
#using beautifulsoup to parse and by default it is html.hence it is necessary to mention the type.
xml = BeautifulSoup(req)
print(xml)
#Iterating the document.
for item in xml.findAll('title'):
    print(item) 