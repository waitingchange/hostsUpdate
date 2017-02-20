import os
import sys




PCBetahosts = '''218.93.127.136 pcbeta.com
218.93.127.136 i.pcbeta.com
218.93.127.136 bbs.pcbeta.com
218.93.127.136 www.pcbeta.com
218.93.127.136 uc.pcbeta.com
218.93.127.136 cdn.pcbeta.static.inimc.com
218.93.127.136 mac.pcbeta.com
218.93.127.136 static.template.pcbeta.com'''

def main():
	hostsFile = open('/etc/hosts', 'a')
	hostsFile.write(PCBetahosts)
	hostsFile.close( )

	os.system('sudo dscacheutil -flushcache')
	os.system('sudo killall -HUP mDNSResponder')

	print 'complete '

if __name__ == '__main__':
	main()