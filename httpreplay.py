from urlparse import urlparse
import urllib
import urllib2
def post(url,headers,content)
#headers:cookie content-type (referer) by httpliveheader
	req=urllib2.Request(url,content,headers)
	resp=urllib2.urlopen(req)

