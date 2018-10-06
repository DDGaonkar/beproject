import requests 
import bs4
res = requests.get('https://www.amazon.in/Power-Your-Subconscious-Mind-Success/dp/8172345666/ref=sr_1_1_sspa?s=books&ie=UTF8&qid=1536939154&sr=1-1-spons&keywords=books&psc=1&smid=A05378423NJE7Q5XCN3XZ')

SOUP = bs4.BeautifulSoup(res.text, 'lxml')

#container = soup.find_all('li',{'id':'SalesRank'})
#container1 = soup.find_all('div', {'class':'content'})
#contain = container1[0].find_all('span', {'class':'a-size-small'})
#no_of_reviews = contain[0].text.strip()
#sales_rank = container[0].text.split('#')[1].split('(')[0]
#container = soup.find_all('div', {'id':'buyNewInner'})
#discount_container[0].find_all('span', {'class':'a-size-base'})[0].text.strip().split(' ')[3].strip()
#rating = soup.find_all('div', {'class':'content'})
#rating = rating[0].find_all('span', {'class':'a-icon-alt'})
#rating = rating[0].text.split(' ')[0]
rating_histo = SOUP.find_all('tr', {'class':'a-histogram-row'})
rating_5 = rating_histo[0].text.split('star')[1].replace('%', '')
rating_4 = rating_histo[1].text.split('star')[1].replace('%', '')
rating_positive = int(rating_5) + int(rating_4)
rating_2 = rating_histo[-2].text.split('star')[1].replace('%', '')
rating_1 = rating_histo[-1].text.split('star')[1].replace('%', '')
rating_negative = int(rating_2) + int(rating_1)