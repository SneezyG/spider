
# A simple web crawler collecting all links in wiki website with duplicate link fitering.


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

links = set()

def getLinks(url):
  global links 
  html = urlopen('http://en.wikipedia.org{}'.format(url))
  bs = BeautifulSoup(html, 'html.parser')
  for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
    if 'href' in link.attrs:
     if link.attrs['href'] not in links:
       newLink = link.attrs['href']
       print(newLink)
       links.add(newLink)
       getLinks(newLink)
       

getLinks('')