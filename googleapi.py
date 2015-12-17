import urllib
import json
from broswer import *
def google(search_term):
	ab = browser()
	search_term = urllib.quote_plus(search_term)
	response = ab.open('http://ajax.googleapis.com/'+\
	'ajax/services/search/web?v=1.0&q=' + search_term)
	objects = json.load(response)
	i=0
	for result in objects['responseData']['results']:
		url = result['url']
		title = result['titleNoFormatting']
		text = result['content']
		print '[+]Result '+str(i)+':'
		print 'url:'+url
		print 'content:'+text
		i=i+1
install_shadowsocks()
google('Violent Python')
