#res = requests.get('https://www.amazon.in/s/ref=sr_pg_2?rh=i%3Aaps%2Ck%3Abooks&page=1&keywords=books')

#"https://www.amazon.in/s/ref=sr_pg_2?rh=i%3Aaps%2Ck%3Abooks&page=1&keywords=books"
# https://www.amazon.in/s/ref=sr_pg_2?rh=n%3A976389031%2Ck%3Abooks&page=2&keywords=books

import requests
import bs4

for i in range(1, 2):
 x= 'https://www.amazon.in/s/ref=sr_pg_'+ str(i) +'?rh=n%3A976389031%2Ck%3Abooks&page=' + str(i) + '&keywords=books'
 print(x)
 res = requests.get(x)
 soup = bs4.BeautifulSoup(res.text, 'lxml')
 containers = soup.find_all('li', 's-result-item') 
 for container in containers:
  try:
   RES = requests.get(container.a['href'])
   SOUP = bs4.BeautifulSoup(RES.text, 'lxml')
   CONTAINER = SOUP.find_all('li',{'id':'SalesRank'})
   print(CONTAINER[0].text.split('#')[1].split('(')[0])
  except:
   pass
