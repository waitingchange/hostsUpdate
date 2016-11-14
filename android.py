import urllib
import os
import sys

url = 'https://coding.net/u/scaffrey/p/hosts/git/raw/master/hosts'


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
	os.system('adb root')
	os.system('adb remount /system')
	os.system('adb push /tmp/hosts /system/etc/hosts')
	# os.system('sudo killall -HUP mDNSResponder')
	print 'complete '

if __name__ == '__main__':
	main()