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
 items = soup.find_all('li', 's-result-item') 
 for item in items:
  try:
   RES = requests.get(item.a['href'])
   SOUP = bs4.BeautifulSoup(RES.text, 'lxml')
   # sales_rank 
   container = SOUP.find_all('li',{'id':'SalesRank'})
   sales_rank = container[0].text.split('#')[1].split('(')[0]
   print(sales_rank)
   # rating (overall customer review ratings)
   rating = SOUP.find_all('div', {'class':'content'})
   rating = rating[0].find_all('span', {'class':'a-icon-alt'})
   rating = rating[0].text.split(' ')[0]
   # positive and negative rating
   rating_histo = SOUP.find_all('tr', {'class':'a-histogram-row'})
   rating_5 = rating_histo[0].text.split('star')[1].replace('%', '')
   rating_4 = rating_histo[1].text.split('star')[1].replace('%', '')
   rating_positive = int(rating_5) + int(rating_4)
   rating_2 = rating_histo[-2].text.split('star')[1].replace('%', '')
   rating_1 = rating_histo[-1].text.split('star')[1].replace('%', '')
   rating_negative = int(rating_2) + int(rating_1)
   # no_of_reviews
   container1 = SOUP.find_all('div', {'class':'content'})
   contain = container1[0].find_all('span', {'class':'a-size-small'})
   no_of_reviews = contain[0].text.strip()
   print(no_of_reviews)
   # discount_value
   container2 = SOUP.find_all('div', {'id':'buyNewInner'})
   discount_value = container2[0].find_all('span', {'class':'a-size-base'})[0].text.strip().split(' ')[3].strip()
   # discount_rate
   discount_rate = container2[0].find_all('span', {'class':'a-size-base'})[0].text.strip().split(' ')[-1]
   print(discount_value)
  except:
   pass
