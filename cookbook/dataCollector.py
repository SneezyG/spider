
# A simple web crawler collecting the title, first-paragraph and edit-link-url across pages of a wiki website.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

links = set()

def getLinks(url):
  global links 
  html = urlopen('http://en.wikipedia.org{}'.format(url))
  bs = BeautifulSoup(html, 'html.parser')
  
  try:
    print(bs.h1.get_text())
    print(bs.find(id ='mw-content-text').find_all('p')[0])
    print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
  except:
    print('This page is missing something! continuing ...')
  
  for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
    if 'href' in link.attrs:
     if link.attrs['href'] not in links:
       newLink = link.attrs['href']
       print('_' * 20)
       print(newLink)
       links.add(newLink)
       getLinks(newLink)
       

getLinks('')

