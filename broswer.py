import socks
import socket
import mechanize
import cookielib
def create_connection(address, timeout=None, source_address=None):
	sock = socks.socksocket()
	sock.connect(address)
	return sock
def install_shadowsocks():
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1080)

	socket.socket = socks.socksocket
	socket.create_connection = create_connection
class browser(mechanize.Browser):
	def __init__(self):
		mechanize.Browser.__init__(self)
		self.set_handle_equiv(True)
		self.set_handle_redirect(True)
		self.set_handle_referer(True)
		self.set_handle_robots(False)

		self.user_agents = ['Mozilla/4.0 ',\
'FireFox/6.01','ExactSearch', 'Nokia7110/1.0']
		self.addheaders=[('User-agent',(self.user_agents[0]))]
		self.cookie_jar = cookielib.LWPCookieJar()
		self.set_cookiejar(self.cookie_jar)
