import urllib
import os
import sys

url = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'


PCBetahosts = '''218.93.127.136 pcbeta.com
218.93.127.136 i.pcbeta.com
218.93.127.136 bbs.pcbeta.com
218.93.127.136 www.pcbeta.com
218.93.127.136 uc.pcbeta.com
218.93.127.136 cdn.pcbeta.static.inimc.com
218.93.127.136 mac.pcbeta.com
218.93.127.136 static.template.pcbeta.com'''


def main():
	page = urllib.urlopen(url)
	html = page.read()
	print html

	keyWord = raw_input( 'please input y/n: ' )
	print 'keyWord is ' , keyWord
	if keyWord != 'y':
		print 'unable to continue!'
		exit()

	print 'continue ...'
	file_object = open('/tmp/hosts', 'w')
	file_object.write(html)
	file_object.write(PCBetahosts)
	file_object.close( )

	os.system('sudo mv /tmp/hosts /etc/hosts')
	os.system('sudo dscacheutil -flushcache')
	os.system('sudo killall -HUP mDNSResponder')

	print 'complete '

if __name__ == '__main__':
	main()