import os
import sys
import platform
import urllib

url = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'




PCBetahosts = '''218.93.127.136 pcbeta.com
218.93.127.136 i.pcbeta.com
218.93.127.136 bbs.pcbeta.com
218.93.127.136 www.pcbeta.com
218.93.127.136 uc.pcbeta.com
218.93.127.136 cdn.pcbeta.static.inimc.com
218.93.127.136 mac.pcbeta.com
218.93.127.136 static.template.pcbeta.com\n'''

def main():

	page = urllib.urlopen(url)
	html = page.read()
	print html

	sysstr = platform.system()
	if(sysstr =="Windows"):
		keyWord = raw_input( 'please input y/n: ' )
		print 'keyWord is ' , keyWord
		if keyWord != 'y':
			print 'unable to continue!'
			exit()

		print 'continue ...'
		file_object = open('C:\\hosts', 'w')
		file_object.write(html)
		file_object.write(PCBetahosts)
		file_object.close( )


		# hostsFile = open('C:\\Windows\\System32\\drivers\\etc\\hosts', 'a')
		# hostsFile.write(PCBetahosts)
		# hostsFile.close( )
		os.system('move C:\\hosts C:\\Windows\\System32\\drivers\\etc\\hosts')

		os.system('ipconfig /flushdns')

	# print 'complete '

if __name__ == '__main__':
	main()