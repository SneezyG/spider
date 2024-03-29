from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re


# A simple web spider collecting both internal and external link from a website.



#Retrieves a list of all Internal links found on a page
def getInternalLinks(bs, includeUrl):

  includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
  internalLinks = []
  #Finds all links that begin with a "/"
  for link in bs.find_all('a',
    href=re.compile('^(/|.*' +includeUrl+')')):
    if link.attrs['href'] is not None:
      if link.attrs['href'] not in internalLinks:
        if(link.attrs['href'].startswith('/')):
          internalLinks.append(includeUrl+link.attrs['href'])
        else:
          internalLinks.append(link.attrs['href'])
          
    return internalLinks


#Retrieves a list of all external links found on a page
def getExternalLinks(bs, excludeUrl):
  externalLinks = []
  #Finds all links that start with "http" that do
  #not contain the current URL
  for link in bs.find_all('a', href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
    if link.attrs['href'] is not None:
      if link.attrs['href'] not in externalLinks:
        externalLinks.append(link.attrs['href'])
  return externalLinks



# Collects a list of all external URLs found on the site
allExtLinks = set()
allIntLinks = set()
def getAllLinks(siteUrl):
  html = urlopen(siteUrl)
  domain = '{}://{}'.format(urlparse(siteUrl).scheme,
   urlparse(siteUrl).netloc)
  bs = BeautifulSoup(html, 'html.parser')
  internalLinks = getInternalLinks(bs, domain)
  externalLinks = getExternalLinks(bs, domain)
  for link in externalLinks:
    if link not in allExtLinks:
      allExtLinks.add(link)
      print(link)
  for link in internalLinks:
    if link not in allIntLinks:
      allIntLinks.add(link)
      getAllLinks(link)
      
allIntLinks.add('http://oreilly.com')
getAllLinks('http://oreilly.com')
