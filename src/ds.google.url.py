import re
import urllib2

from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=python'
headers = {'User-Agent' : 'Mozilla 5.0'}
request = urllib2.Request(url, None, headers)
response = urllib2.urlopen(request)
bfs = BeautifulSoup(response.read(), 'html.parser')

nodes=bfs.select("#ires > ol > div > h3 > a")
print "http url의갯수?",len(nodes)
for i, node in enumerate(nodes):
    print i+1, str(node.get('href')).split('q=')[1]