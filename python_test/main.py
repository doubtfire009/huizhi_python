import urllib.request
import urllib.error
response = urllib.request.urlopen('http://www.mayhomer.com/')
html = response.read()  
print(html)