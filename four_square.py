import requests
import sys
from bs4 import BeautifulSoup
import pandas as pd
r = requests.get('https://foursquare.com/explore?mode=url&near=Mangalore%2C%20Karn%C4%81taka%2C%20India&nearGeoId=72057594039191716&q=Food')
content = r.content.decode(encoding='UTF-8')
soup = BeautifulSoup(r.content.decode(encoding='UTF-8'), "lxml")
score_full = soup.find_all('div', {"class": "venueScore positive"})
name_full =soup.find_all('div',{'class':'venueName'})
address_full=soup.find_all('div',{'class' : "venueAddress" })
review_full=soup.find_all('ul',{'class':'tips'})
name =[]
score = []
address=[]
review=[]
for item in name_full: 
    name.append(item.text)
for k in address_full:
	address.append(k.text)
for l in score_full:
	score.append(l.text)
for m in review_full:
	review.append(m.text)

name=name[0:20]
address=address[0:20]
score=score[0:20]
review=review[0:20]
print(name)
print(address)
print(score)
print(review)
output = pd.DataFrame({'NAME':name,'RATING' : score,'ADDRESS': address,'REVIEW':review})

output.index.name='sno'
output.to_csv("foursquare.csv",index= True)



