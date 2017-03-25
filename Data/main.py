import re

f=open('input.txt','r')
_in=f.read()
f.close()

from bs4 import BeautifulSoup

soup=BeautifulSoup(_in,'html.parser')

i=0
for element in soup.findAll('div',{'data-type':'comment'}):
	if ('harrypotter' == element['data-subreddit']):
		keep_going=False
		try:
			print(element.findAll('p').text)
		except:
			pass
		for paragraph in element.findAll('p'):
			try:
				print(paragraph.text)
				if 'Quote starting with' in paragraph.text:
					keep_going=True
					break
			except Exception as e:
				print('error',e)

		if keep_going == True:
			#get time
			for time in element.findAll('time'):
				date=time['datetime']
				break
			i+=1
			print('Date: ',re.sub('T.+','',date))
			print(element.text)
			#, re.sub('.+?T','',date)[:8],'\t',element.findAll('span',{'class':'score likes'})[0].text[0])