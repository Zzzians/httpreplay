import broswer
from BeautifulSoup import BeautifulSoup
import os
def mirror(url,dir):
	br=broswer.browser()
	html=br.open(url)
	soup=BeautifulSoup(html)
	images=soup.findAll('img')
	for image in images:
		filename=image['src'].lstrip('http://')
		filename=filename.replace('/','_')
		filename=os.path.join(dir,filename)
		data=br.open(image['src']).read()
		br.back()
		save=open(filename,'wb')
		save.write(data)
		save.close()
mirror('https://shtech.org/gradebot/scoreboard?sidd=1200185529&sid=1872699482&courseid=1&homeworkid=1','./imgs')
