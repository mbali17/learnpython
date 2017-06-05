'''
urlib is a builtin library for connecting to a remote server on the internet and
obtain data from it.
'''
#Step1:urllib is a package.
import urllib.request as req
#step2:use the urlopen method and pass the URL to be opened.
request = req.urlopen("https://www.asianpaints.com")
#step3:For now print the data recieved.
print(20*"#")
print(request.read())
