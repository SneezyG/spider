from bs4 import BeautifulSoup
import requests
import re

# Crawling a site through links

class Content:
  """
  create object out of collected info and define how to print them.
  """
  def __innit__(self, url, title, body):
    self.url = url
    self.title = title
    self.body = body

  def print(self):
    """
     smart printing function controls output
    """
    print("URL: {}".format(self.url))
    print("TITLE: {}".format(self.title))
    print("BODY:\n{}".format(self.body))
  
  

class Website:
  def __init__(self, name, url, targetPattern, absoluteUrl, titleTag, bodyTag):
      self.name = name
      self.url = url
      self.targetPattern = targetPattern
      self.absoluteUrl=absoluteUrl
      self.titleTag = titleTag
      self.bodyTag = bodyTag



class Crawler:
  def __init__(self, site):
    self.site = site
    self.visited = []
   
  def getPage(self, url):
    try:
      req = requests.get(url)
    except requests.exceptions.RequestException:
      return None 
    return BeautifulSoup(req.text, 'html.parser')
    
  def parse(self, url):
    bs = self.getPage(url)
    if bs is not None:
      title = self.safeGet(bs, self.site.titleTag)
      body = self.safeGet(bs, self.site.bodyTag)
    if title != '' and body != '':
      content = Content(url, title, body)
      content.print()
      
  def crawl(self):
    """
    Get pages from website home page
    """
    
    bs = self.getPage(self.site.url)
    targetPages = bs.findAll('a', href=re.compile(self.site.targetPattern))
    print(targetPages)
    for targetPage in targetPages:
      targetPage = targetPage.attrs['href']
      if targetPage not in self.visited:
        self.visited.append(targetPage)
        if not self.site.absoluteUrl:
          targetPage = '{}{}'.format(self.site.url, targetPage)
          self.parse(targetPage)
          
          
reuters = Website('Reuters', 'https://www.reuters.com', '^(/article/)', False,
 'h1', 'div.StandardArticleBody_body_1gnLA')

crawler = Crawler(reuters)
crawler.crawl()
