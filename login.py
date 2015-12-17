import broswer
import re
br=broswer.browser()
broswer.install_shadowsocks()
page=br.open("http://shtech.org/gradebot")
linker=re.compile('href="(.*?)"')
html=page.read()
br.select_form(nr = 0)
br['email']='#'
br['password']='#'
resp=br.submit().read()
print resp
