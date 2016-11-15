import urllib
import os
import sys

url = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'


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
	file_object.close( )

	os.system('sudo mv /tmp/hosts /etc/hosts')
	os.system('sudo killall -HUP mDNSResponder')
	print 'complete '

if __name__ == '__main__':
	main()