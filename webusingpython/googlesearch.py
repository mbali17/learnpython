'''
    performing search query on google using urllib
'''
import urllib.request
#this library is used to encode/parse the data to be passed or response to be read
import urllib.parse as parse


values = {'q':'is machine learning useful'}
#Encoding the value to be searched since it can contain spaces as well.
data = parse.urlencode(values)
urlToConnect = 'https://www.google.com/webhp#'+data;
print(urlToConnect)
req = urllib.request.Request(urlToConnect)
resp = urllib.request.urlopen(req)
resp_data = resp.read();

print(resp_data)
