import requests
import os
import json
from bs4 import BeautifulSoup
import urllib2

resp = urllib2.urlopen("http://hckrnews.com/data/")
soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))

links = []
for link in soup.find_all('a', href=True):
  links.append(link['href'])

linksNo = len(links)

for i, l in enumerate(links):
  # skip first link as it is '../' and only save the data which doesn't exist
  if (i != 0 and not os.path.exists("./data/%son" % (l))):
    filename = './data/' + l + 'on'
    f = open(filename, 'w')
    url = "http://hckrnews.com/data/%s" % (l)
    rs = requests.get(url)
    dailynews = rs.text.encode('utf-8')
    f.write(dailynews)
    f.close
    print "============ " + str(i) + "/" + str(linksNo) + " ============\r",