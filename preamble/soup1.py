
from urllib.request import urlopen
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


def parser(html):
  bs = BeautifulSoup(html.read(), 'html.parser')
  try: 
    title = bs.body.h1
  except AttributeError as e:
    print(' h1 parent-tag was not found')
  else:
    if title is None:
      print('h1 tag was found')
    else:
      print(title)


try: 
  html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
  print(e)
except URLError as e:
  print("server not found or currently down")
else:
  parser(html)
  
 