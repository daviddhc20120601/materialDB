import socket
def getIp():
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	try:
		s.connect(("www.baidu.com" ,0))
		ip=s.getsockname()[0]
	except:
		return "127.0.0.1"
	finally:
		s.close()
	return ip
print getIp()
	
